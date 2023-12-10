/**
 * @file gray2color.cc
 * @brief  ./gray2color.py c++重写
 * @author M0rtzz E-mail : m0rtzz@163.com
 * @version 1.0
 * @date 2023-11-06
 *
 */

#include <iostream>
#include <string>
#include <filesystem>
#include <chrono>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;
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
        int hours = int(seconds / 3600);
        int minutes = int((seconds - hours * 3600) / 60);
        int secs = int(seconds - hours * 3600 - minutes * 60);

        return to_string(hours) + "h " + to_string(minutes) + "m " + to_string(secs) + "s";
    }
};

/**
 * @brief  单通道转 RGB 通道
 * @param  img_path
 * @param  color_map
 */
void grayToColor(const string &img_path, const Mat &color_map)
{
    // 读取图片
    Mat gray_img = imread(img_path, IMREAD_GRAYSCALE);
    // 判断彩色图片是否已经存在
    fs::path path(img_path);
    string save_dir = "./images/my_images/fisheye_dataset/semantic_segmentation_CityScapesPalette";
    if (!fs::exists(save_dir))
    {
        fs::create_directory(save_dir);
    }
    string save_path = (save_dir / path.filename()).replace_extension(".png");
    if (fs::exists(save_path))
    {
        return;
    }

    // double min_val, max_val;
    // Point min_loc, max_loc;
    // minMaxLoc(gray_img, &min_val, &max_val, &min_loc, &max_loc);
    // cout << " " << min_val << " " << max_val << '\n';

    // 像素赋值
    int h = gray_img.rows;
    int w = gray_img.cols;
    Mat color_img(h, w, CV_8UC3, Scalar(0, 0, 0));
    for (int i = 0; i < color_map.rows; i++)
    {
        Mat index;
        findNonZero(gray_img == i, index);
        for (int j = 0; j < index.total(); j++)
        {
            Point pt = index.at<Point>(j);
            color_img.at<Vec3b>(pt) = color_map.at<Vec3b>(i);
        }
    }
    // 保存图片
    cvtColor(color_img, color_img, COLOR_BGR2RGB);
    imwrite(save_path, color_img);
}

int main()
{
    // 你的colormap
    Mat cmap = (Mat_<Vec3b>(24, 1) << Vec3b(0, 0, 0), // unlabeled  0
                Vec3b(128, 64, 128),                  // road  1
                Vec3b(244, 35, 232),                  // sidewalk  2
                Vec3b(70, 70, 70),                    // building  3
                Vec3b(102, 102, 156),                 // wall  4
                Vec3b(190, 153, 153),                 // fence  5
                Vec3b(153, 153, 153),                 // pole  6
                Vec3b(250, 170, 30),                  // traffic light  7
                Vec3b(220, 220, 0),                   // traffic sign  8
                Vec3b(107, 142, 35),                  // vegetation  9
                Vec3b(152, 251, 152),                 // terrain  10
                Vec3b(70, 130, 180),                  // sky  11
                Vec3b(220, 20, 60),                   // pedestrian  12
                Vec3b(255, 0, 0),                     // rider  13
                Vec3b(0, 0, 142),                     // Car  14
                Vec3b(0, 0, 70),                      // truck  15
                Vec3b(0, 60, 100),                    // bus  16
                // NOTE: 执行完 ./change_index 之后，需要加以修改
                // Vec3b(0, 0, 0),                       // train
                Vec3b(81, 0, 81),     // ground  17
                Vec3b(0, 0, 230),     // motorcycle  18
                Vec3b(119, 11, 32),   // bicycle  19
                Vec3b(110, 190, 160), // static  20
                Vec3b(170, 120, 50),  // dynamic  21
                Vec3b(55, 90, 80),    // other  22
                // Vec3b(45, 60, 150), // water  23
                Vec3b(157, 234, 50) // road line  24
                                    // Vec3b(81, 0, 81)      // ground  25
    );
    // 文件路径
    string img_dir = "./images/my_images/fisheye_dataset/semantic_segmentation_raw";
    if (!fs::exists(img_dir))
    {
        fs::create_directory(img_dir);
    }
    int total_images = count_if(fs::directory_iterator(img_dir), fs::directory_iterator(), [](const fs::directory_entry &entry)
                                { return entry.path().extension() == ".png"; });
    ProgressBar progress(total_images);
    for (const fs::directory_entry &entry : fs::directory_iterator(img_dir))
    {
        if (!entry.is_regular_file() || entry.path().extension() != ".png")
        {
            continue;
        }
        grayToColor(entry.path().string(), cmap);
        progress.updateTime();
    }
    cout << endl;
    return 0;
}
