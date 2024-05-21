/**
 * @file PT2fisheye.cc
 * @brief  origin2fisheye
 * @author M0rtzz E-mail : m0rtzz@outlook.com
 * @version 1.0
 * @date 2024-01-22
 *
 */

#include <chrono>
#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;
namespace fs = filesystem;

/**
 * @brief  显示剩余时间
 */
class ProgressBar
{
public:
    explicit ProgressBar(int total, int width = 45) : total(total), width(width), start_time(std::chrono::high_resolution_clock::now()), progress(0) {}

    void updateTime()
    {
        ++progress;
        int remaining = total - progress;

        float percentage = static_cast<float>(progress) / total;
        int filled_width = static_cast<int>(width * percentage);

        std::chrono::duration<double> elapsed_seconds = std::chrono::high_resolution_clock::now() - start_time;
        double speed = elapsed_seconds.count() / progress;
        std::chrono::duration<double> remaining_time = std::chrono::duration<double>(speed * remaining);

        cout << "\r"
             << "[" << string(filled_width, '#') << string(width - filled_width, ' ') << "] "
             << int(percentage * 100.0) << "% "
             << "Remaining Time: " << formatTime(remaining_time.count()) << flush;
    }

private:
    int total;
    int width;
    std::chrono::time_point<std::chrono::high_resolution_clock> start_time;
    int progress;

    string formatTime(double seconds)
    {
        int hours = static_cast<int>(seconds / 3600);
        int minutes = static_cast<int>((seconds - hours * 3600) / 60);
        int secs = static_cast<int>(seconds - hours * 3600 - minutes * 60);

        return to_string(hours) + "h " + to_string(minutes) + "m " + to_string(secs) + "s";
    }
};

/**
 * @brief  将标准图像中的点坐标转换为鱼眼图像中的点坐标
 * @param  xd
 * @param  yd
 * @param  xc
 * @param  yc
 * @param  f
 * @param  xx
 * @param  yy
 */
void changePoints(int xd, int yd, int xc, int yc, int f, int &xx, int &yy)
{
    int x = xd - xc;
    int y = yd - yc;
    double rc = sqrt(x * x + y * y);
    double st = 0;
    if (rc != 0 && f != 0)
    {
        st = atan(rc / f);
    }
    double rf = f * st;
    if (rc == 0)
    {
        xx = 0;
        yy = 0;
    }
    else
    {
        xx = static_cast<int>(rf * x / rc);
        yy = static_cast<int>(rf * y / rc);
    }
    xx += xc;
    yy += yc;
}

/**
 * @brief  将标准图像转换为鱼眼图像
 * @param  img: 图片
 * @param  pointx: 中心x坐标
 * @param  pointy: 中心y坐标
 */
Mat getOneFisheye(Mat img, int pointx, int pointy)
{
    int height = img.rows;
    int width = img.cols;
    Mat result(height, width, CV_8UC3, Scalar(0, 0, 0));
    int xc = pointx + width / 2;
    int yc = pointy + height / 2;
    int f = 159;
    for (int dy = 0; dy < height; ++dy)
    {
        for (int dx = 0; dx < width; ++dx)
        {
            int x = pointx + dx;
            int y = pointy + dy;
            int xx, yy;
            changePoints(x, y, xc, yc, f, xx, yy);
            xx -= pointx;
            yy -= pointy;
            result.at<Vec3b>(yy, xx) = img.at<Vec3b>(y, x);
        }
    }
    return result;
}

/**
 * @brief  批处理
 * @param  image_paths
 * @param  target_dir
 */
void processImages(vector<string> &image_paths, string target_dir)
{
    if (!fs::exists(target_dir))
    {
        fs::create_directories(target_dir);
    }

    ProgressBar process(image_paths.size());

    for (const auto &img_path : image_paths)
    {
        string image_file = fs::path(img_path).filename().string();
        string target_path = fs::path(target_dir) / image_file;

        Mat img = imread(img_path);
        Mat result = getOneFisheye(img, 0, 0);
        result = result(Rect(704, 274, 640, 576)).clone(); // 裁剪成正方形
        imwrite(target_path, result);

        process.updateTime();
    }
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        cerr << "Usage: " << argv[0] << " image_paths..." << endl;
        return EXIT_FAILURE;
    }

    vector<string> image_paths;
    for (int i = 1; i < argc; ++i)
    {
        image_paths.push_back(argv[i]);
    }

    string target_dir = "./images/my_images/fisheye_transformation/normal2fisheye/";
    processImages(image_paths, target_dir);

    cout << endl;

    return EXIT_SUCCESS;
}
