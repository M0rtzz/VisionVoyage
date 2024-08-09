/**
 * @file cubemap2fisheye.cc
 * @brief  ./cubemap2fisheye.py c++重写
 * @author M0rtzz E-mail : m0rtzz@outlook.com
 * @version 1.0
 * @date 2024-02-03
 *
 */

#include <Eigen/Dense>
#include <algorithm>
#include <cmath>
#include <filesystem>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <string>
#include <tuple>
#include <vector>

using namespace std;
using namespace cv;

/**
 * @brief  将字符串转换为小写
 * @param  str
 * @return string
 */
string toLower(const string &str)
{
    string lowerStr = str;
    transform(str.begin(), str.end(), lowerStr.begin(),
              [](char c)
              { return c >= 'A' && c <= 'Z' ? c + 32 : c; });
    return lowerStr;
}

/**
 * @brief  比较函数，按照特定顺序排序
 * @param  a
 * @param  b
 * @return true
 * @return false
 */
bool compareImageNames(const string &a, const string &b)
{
    vector<string> order = {"left", "right", "top", "bottom", "front"};

    string lower_a = toLower(a);
    string lower_b = toLower(b);

    vector<int> priorityA(5, 0), priorityB(5, 0);

    for (int i = 0; i < order.size(); ++i)
    {
        if (lower_a.find(order[i]) != string::npos)
        {
            priorityA[i] = 1;
        }
        if (lower_b.find(order[i]) != string::npos)
        {
            priorityB[i] = 1;
        }
    }
    return lexicographical_compare(priorityA.begin(), priorityA.end(), priorityB.begin(), priorityB.end(), greater<int>());
}

/**
 * @brief  获取当前时间并格式化字符串
 * @return string
 */
string currentTimeFormatted()
{
    auto now = chrono::system_clock::now();
    auto in_time_t = chrono::system_clock::to_time_t(now);

    stringstream ss;
    ss << put_time(localtime(&in_time_t), "%Y-%m-%d_%H:%M:%S");
    return ss.str();
}

/**
 * @brief  生成基于图像尺寸的球面坐标
 * @param  fish_size -- 鱼眼图像的尺寸
 * @return pair<Eigen::MatrixXd, Eigen::MatrixXd> -- 包含两个矩阵的pair，分别代表r和phi坐标
 */
pair<Eigen::MatrixXd, Eigen::MatrixXd> getSphericalCoordinates(int fish_size)
{
    int center = fish_size / 2;
    Eigen::MatrixXd xx = Eigen::MatrixXd::Zero(fish_size, fish_size);
    Eigen::MatrixXd yy = Eigen::MatrixXd::Zero(fish_size, fish_size);

    for (int i = 0; i < fish_size; ++i)
    {
        for (int j = 0; j < fish_size; ++j)
        {
            xx(i, j) = j - center;
            yy(i, j) = center - i; // 注意Y轴在图像中向下是正方向
        }
    }

    xx /= center;
    yy /= center;

    Eigen::MatrixXd r = (xx.array().square() + yy.array().square()).sqrt();
    r = r.unaryExpr([](double v)
                    { return (v <= 1.0) ? v : nan(""); });

    Eigen::MatrixXd phi = Eigen::MatrixXd::Zero(fish_size, fish_size);
    for (int i = 0; i < fish_size; ++i)
    {
        for (int j = 0; j < fish_size; ++j)
        {
            if (!isnan(r(i, j)) && r(i, j) > 0)
            {
                phi(i, j) = atan2(yy(i, j), xx(i, j));
            }
        }
    }

    return {r, phi};
}

/**
 * @brief  将球面坐标转换为笛卡尔坐标
 * @param  r -- 球面坐标中的r矩阵
 * @param  phi -- 球面坐标中的phi矩阵
 * @param  FOV -- 视场(Field of View)
 * @return tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::MatrixXd> -- 包含x, y, z坐标矩阵的元组
 */
tuple<Eigen::MatrixXd, Eigen::MatrixXd, Eigen::MatrixXd> sphericalToCartesian(const Eigen::MatrixXd &r, const Eigen::MatrixXd &phi, double FOV)
{
    Eigen::MatrixXd theta = r * FOV / 2;
    Eigen::MatrixXd x = theta.unaryExpr([](double v)
                                        { return sin(v); })
                            .array() *
                        phi.unaryExpr([](double v)
                                      { return cos(v); })
                            .array();
    Eigen::MatrixXd y = theta.unaryExpr([](double v)
                                        { return sin(v); })
                            .array() *
                        phi.unaryExpr([](double v)
                                      { return sin(v); })
                            .array();
    Eigen::MatrixXd z = theta.unaryExpr([](double v)
                                        { return cos(v); });

    return {x, y, z};
}

/**
 * @brief  根据笛卡尔坐标确定点所在的立方体表面
 * @param  x
 * @param  y
 * @param  z
 * @return string -- 点所在的立方体表面名称
 */
string getFace(double x, double y, double z)
{
    double max_axis = max({abs(x), abs(y), abs(z)});
    if (abs(x) == max_axis)
    {
        return x < 0 ? "right" : "left";
    }
    else if (abs(y) == max_axis)
    {
        return y < 0 ? "bottom" : "top";
    }
    else
    {
        return z < 0 ? "back" : "front";
    }
}

/**
 * @brief  计算立方体表面上的u, v坐标
 * @param  face
 * @param  x
 * @param  y
 * @param  z
 * @return pair<double, double> -- 立方体表面上的u, v坐标
 */
pair<double, double> rawFaceCoordinates(const string &face, double x, double y, double z)
{
    double u, v, ma;
    if (face == "left" || face == "right")
    {
        u = (face == "left") ? z : -z;
        v = -y;
        ma = abs(x);
    }
    else if (face == "bottom" || face == "top")
    {
        u = -x;
        v = (face == "bottom") ? -z : z;
        ma = abs(y);
    }
    else
    { // "back" or "front"
        u = (face == "front") ? -x : x;
        v = -y;
        ma = abs(z);
    }
    return {(u / ma + 1) / 2, (v / ma + 1) / 2};
}

/**
 * @brief  将立方体表面上的坐标转换为2D图像上的坐标
 * @param  face -- 点所在的立方体表面名称
 * @param  u -- 立方体表面上的u坐标
 * @param  v -- 立方体表面上的v坐标
 * @param  pic_size -- 图像尺寸
 * @return pair<int, int> -- 2D图像上的坐标
 */
pair<int, int> normalizedCoordinates(const string &face, double u, double v, int pic_size)
{
    map<string, pair<int, int>> face_origin = {
        {"left", {0, pic_size}},
        {"front", {pic_size, pic_size}},
        {"right", {2 * pic_size, pic_size}},
        {"back", {3 * pic_size, pic_size}},
        {"top", {pic_size, 0}},
        {"bottom", {pic_size, 2 * pic_size}}};

    auto [face_x, face_y] = face_origin[face];
    int x = floor(u * pic_size);
    int y = floor(v * pic_size);

    x = clamp(x, 0, pic_size - 1);
    y = clamp(y, 0, pic_size - 1);

    return {face_x + x, face_y + y};
}

/**
 * @brief  将立方体映射图像转换为鱼眼图像
 * @param  picture_group -- 包含立方体六个面图像的向量
 * @param  pic_size -- 立方体贴图每个面的尺寸
 * @param  fish_size -- 鱼眼图像的尺寸
 * @param  FOV -- 视场(Field of View)
 * @return Mat -- 鱼眼图像
 */
Mat cube2Fisheye(const vector<Mat> &picture_group, int pic_size, int fish_size, double FOV)
{
    Mat cubemap(3 * pic_size, 3 * pic_size, CV_8UC3, Scalar(0, 0, 0));
    // 将输入的图像复制到立方体贴图的相应位置
    picture_group[0].copyTo(cubemap(Rect(0, pic_size, pic_size, pic_size)));            // left
    picture_group[1].copyTo(cubemap(Rect(2 * pic_size, pic_size, pic_size, pic_size))); // right
    picture_group[2].copyTo(cubemap(Rect(pic_size, 0, pic_size, pic_size)));            // top
    picture_group[3].copyTo(cubemap(Rect(pic_size, 2 * pic_size, pic_size, pic_size))); // bottom
    picture_group[4].copyTo(cubemap(Rect(pic_size, pic_size, pic_size, pic_size)));     // front

    auto [r, phi] = getSphericalCoordinates(fish_size);
    auto [x, y, z] = sphericalToCartesian(r, phi, FOV * M_PI / 180);

    Mat fisheye_picture = Mat::zeros(fish_size, fish_size, CV_8UC3);
    for (int i = 0; i < fish_size; ++i)
    {
        for (int j = 0; j < fish_size; ++j)
        {
            if (isnan(r(i, j)))
            {
                continue;
            }

            string face = getFace(x(i, j), y(i, j), z(i, j));
            auto [u, v] = rawFaceCoordinates(face, x(i, j), y(i, j), z(i, j));
            auto [x_cubemap, y_cubemap] = normalizedCoordinates(face, u, v, pic_size);

            fisheye_picture.at<Vec3b>(i, j) = cubemap.at<Vec3b>(y_cubemap, x_cubemap);
        }
    }

    return fisheye_picture;
}

int main(int argc, char **argv)
{
    if (argc != 6)
    {
        cerr << "Usage: cube2Fisheye <image> <image> <image> <image> <image>" << endl;
        return EXIT_FAILURE;
    }

    vector<string> image_paths;
    for (int i = 1; i < argc; ++i)
    {
        image_paths.push_back(argv[i]);
    }

    sort(image_paths.begin(), image_paths.end(), compareImageNames);

    vector<Mat> input_images;
    for (const auto &imagePath : image_paths)
    {
        input_images.push_back(imread(imagePath));
    }

    int pic_size = 1024;  // 立方体贴图每个面的尺寸
    int fish_size = 1344; // 鱼眼图像尺寸
    double FOV = 196;     // 鱼眼视角

    Mat fisheye_picture = cube2Fisheye(input_images, pic_size, fish_size, FOV);

    string output_file_name = "./images/my_images/fisheye_transformation/cubemap2fisheye/" + currentTimeFormatted() + ".png";
    imwrite(output_file_name, fisheye_picture);

    // cout << "\n转换成功，文件保存为: " << output_file_name << endl;

    return EXIT_SUCCESS;
}
