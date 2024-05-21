/**
 * @file change_index.cc
 * @brief  ./changeIndex.py c++重写
 * @author M0rtzz E-mail : m0rtzz@outlook.com
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
    explicit ProgressBar(int total, int width = 45) : total(total), width(width), start_time(std::chrono::high_resolution_clock::now()) {}

    void updateTime(int progress)
    {
        int current = progress;
        int remaining = total - progress;

        float percentage = static_cast<float>(progress) / total;
        int filled_width = static_cast<int>(width * percentage);

        std::chrono::duration<double> elapsed_seconds = std::chrono::high_resolution_clock::now() - start_time;
        double speed = elapsed_seconds.count() / (progress + 1);
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

    string formatTime(double seconds)
    {
        int hours = int(seconds / 3600);
        int minutes = int((seconds - hours * 3600) / 60);
        int secs = int(seconds - hours * 3600 - minutes * 60);

        return to_string(hours) + "h " + to_string(minutes) + "m " + to_string(secs) + "s";
    }
};

/**
 * @brief  切换标签
 * @param  img
 * @return Mat
 */
Mat changeIndex(Mat img, bool is_second = true)
{
    int height = img.rows;
    int width = img.cols;
    Mat result(height, width, CV_8UC1);

    for (int dy = 0; dy < height; dy++)
    {
        for (int dx = 0; dx < width; dx++)
        {
            if (is_second == false && img.at<uchar>(dy, dx) == 25)
            {
                result.at<uchar>(dy, dx) = 17;
            }
            else if (is_second == false && img.at<uchar>(dy, dx) == 23)
            {
                result.at<uchar>(dy, dx) = 22;
            }
            else if (is_second == true && img.at<uchar>(dy, dx) == 24)
            {
                result.at<uchar>(dy, dx) = 23;
            }
            else
            {
                result.at<uchar>(dy, dx) = img.at<uchar>(dy, dx);
            }
        }
    }
    return result;
}

/**
 * @brief  处理图像
 * @param  source_dir
 * @param  target_dir
 * @param  keyword
 */
void processImages(string source_dir, string target_dir, string keyword, bool is_second = false)
{
    if (!fs::exists(target_dir))
    {
        fs::create_directories(target_dir);
    }

    int total_images = 0;
    for (const auto &entry : fs::directory_iterator(source_dir))
    {
        string image_file = entry.path().filename().string();
        if (image_file.find(keyword) != string::npos)
        {
            total_images++;
        }
    }

    ProgressBar progressBar(total_images);

    int progress = 0;
    for (const auto &entry : fs::directory_iterator(source_dir))
    {
        string image_file = entry.path().filename().string();
        if (image_file.find(keyword) == string::npos)
        {
            continue;
        }

        string img_path = entry.path().string();
        string target_path = target_dir + "/" + image_file;

        // if (fs::exists(target_path))
        // {
        //     continue;
        // }

        Mat img = imread(img_path, IMREAD_GRAYSCALE);

        // double min_val, max_val;
        // Point min_loc, max_loc;
        // minMaxLoc(img, &min_val, &max_val, &min_loc, &max_loc);
        // cout << " " << min_val << " " << max_val << '\n';

        Mat result = changeIndex(img, is_second);
        imwrite(target_path, result);

        progress++;
        progressBar.updateTime(progress);
    }
}

int main()
{
    string keyword = ".png";

    string source_dir_1 = "./images/my_images/fisheye_dataset/semantic_segmentation_raw";
    string target_dir_1 = "./images/my_images/fisheye_dataset/semantic_segmentation_raw_changed_index";
    processImages(source_dir_1, target_dir_1, keyword, false);
    cout << endl;
    cout << "第一轮转换标签已结束" << endl;

    string source_dir_2 = target_dir_1;
    string target_dir_2 = source_dir_2;
    processImages(source_dir_2, target_dir_2, keyword, true);
    cout << endl;
    cout << "第二轮转换标签已结束" << endl;
    return 0;
}
