#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <hpdf.h>
#include <iostream>

using namespace std;
namespace fs = filesystem;

/**
 * @brief 错误处理函数，用于处理 HPDF 库的错误
 * @param error_code
 * @param error_detail
 * @param user_data
 */
void handleError(HPDF_STATUS error_code, HPDF_STATUS error_detail, void *user_data)
{
    fprintf(stderr, "ERROR: error_code=%04X, error_detail=%d\n", (unsigned int)error_code, (int)error_detail);
    exit(EXIT_FAILURE);
}

// /**
//  * @brief 获取 UNIX 时间戳
//  * @return string
//  */
// string getUnixTimestamp()
// {
//     time_t info = time(0);
//     string formatted_info = "UNIX Timestamp: " + to_string(info);
//     return formatted_info;
// }

/**
 * @brief 格式化时间戳
 * @return string
 */
string getFormattedTimestamp()
{
    time_t now = time(0);
    char buffer[80];
    struct tm *timeinfo;
    timeinfo = localtime(&now);
    strftime(buffer, sizeof(buffer), "PDF Creation Time: %Y/%m/%d_%H:%M:%S", timeinfo);
    return buffer;
}

/**
 * @brief 将文本文档转换为 PDF, 里面参数测试了很长时间, 懒得再测了
 * @param  input_file_path
 * @param  output_pdf_path
 * @return true
 * @return false
 */
bool fromTextDocumentToPDF(const string &input_file_path, const string &output_pdf_path)
{
    ifstream input_file(input_file_path);
    if (!input_file)
    {
        cerr << "Unable to open input file" << endl;
        return EXIT_FAILURE;
    }

    // 创建 PDF 对象
    HPDF_Doc pdf = HPDF_New(handleError, NULL);
    if (!pdf)
    {
        cerr << "Unable to create PDF object" << endl;
        return EXIT_FAILURE;
    }

    // NOTE: 设置字体编码格式为 UTF-8，否则中文字体显示为乱码（注意：只能使用宋体和黑体两种汉字）
    HPDF_UseUTFEncodings(pdf);
    HPDF_SetCurrentEncoder(pdf, "UTF-8");

    // 设置字体并创建新页面
    const char *load_simhei = HPDF_LoadTTFontFromFile(pdf, "./assets/fonts/simhei.ttf", HPDF_TRUE);
    const char *load_fira_code = HPDF_LoadTTFontFromFile(pdf, "./assets/fonts/FiraCode-Medium.ttf", HPDF_TRUE);

    HPDF_Font get_simhei = HPDF_GetFont(pdf, load_simhei, "UTF-8");
    HPDF_Font get_fira_code = HPDF_GetFont(pdf, load_fira_code, "UTF-8");

    // 获取当前时间
    string timestamp = getFormattedTimestamp();
    // string info = getUnixTimestamp();
    string left_top_text = "Created By VisionVoyage";
    // 添加第一页并绘制时间戳和页码
    HPDF_Page page = HPDF_AddPage(pdf);
    HPDF_Page_SetSize(page, HPDF_PAGE_SIZE_A4, HPDF_PAGE_PORTRAIT);

    // 设置 UNIX 时间戳和北京时间的属性
    // NOTE: 经测试，鄙人认为这几个参数效果最好
    HPDF_Font timestamp_font = get_fira_code; // 使用 FiraCode 字体
    float timestamp_font_size = 10;
    float timestamp_x = HPDF_Page_GetWidth(page) - 250; // 将时间戳往左移动
    float timestamp_y = HPDF_Page_GetHeight(page) - 20; // 调整时间戳在垂直方向上的位置

    // NOTE: 经测试，鄙人认为这几个参数效果最好
    HPDF_Font info_font = get_fira_code; // 使用 FiraCode 字体
    float info_font_size = 10;
    float info_x = HPDF_Page_GetWidth(page) - 580; // 将时间戳往左移动
    float info_y = HPDF_Page_GetHeight(page) - 20; // 调整时间戳在垂直方向上的位置

    int page_number = 1;

    // 在第一页右上角绘制北京时间
    HPDF_Page_BeginText(page);
    HPDF_Page_SetFontAndSize(page, timestamp_font, timestamp_font_size);
    HPDF_Page_TextOut(page, timestamp_x, timestamp_y, timestamp.c_str());
    HPDF_Page_EndText(page);

    // 在第一页左上角绘制 UNIX 时间戳
    HPDF_Page_BeginText(page);
    HPDF_Page_SetFontAndSize(page, info_font, info_font_size);
    HPDF_Page_TextOut(page, info_x, info_y, left_top_text.c_str());
    HPDF_Page_EndText(page);

    // 在第一页最下方的中间绘制页码
    HPDF_Page_BeginText(page);
    string page_number_text = "Page " + to_string(page_number);
    float page_number_x = HPDF_Page_GetWidth(page) / 2;
    float page_number_y = 20;
    // NOTE: 经测试，页码为单位数时，鄙人认为这个参数 23.0 效果最好，双位数效果一般，但眼看花了，就暂时搁置了
    HPDF_Page_TextOut(page, page_number_x - 23.0, page_number_y, page_number_text.c_str());
    HPDF_Page_EndText(page);

    page_number++;

    float current_y = HPDF_Page_GetHeight(page) - 50;

    // 从输入文件读取文本并写入到 PDF 中
    string line;
    while (getline(input_file, line))
    {
        HPDF_Page_BeginText(page);

        // 根据语言确定字体
        HPDF_Font font;
        if (line.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos)
        {
            font = get_fira_code; // 英文使用 Fira Code
        }
        else
        {
            font = get_simhei; // 中文使用黑体
        }

        HPDF_Page_SetFontAndSize(page, font, 12);

        // NOTE: 插入换页符，限制每行最多显示 83 个字符，经测试这个参数 83 和 17.5 效果最好
        const int max_line_length = 83;
        for (int i = 0; i < line.length(); i += max_line_length)
        {
            string sub_line = line.substr(i, max_line_length);
            float line_y = current_y - (i / max_line_length) * 17.5;
            HPDF_Page_TextOut(page, 50, line_y, sub_line.c_str());
        }

        HPDF_Page_EndText(page);

        // 更新当前的y坐标
        current_y -= (line.length() / max_line_length + 1) * 17.5;

        // 如果当前页面的剩余空间不足，添加新页面并绘制时间戳和页码
        if (current_y < 50)
        {
            page = HPDF_AddPage(pdf);
            HPDF_Page_SetSize(page, HPDF_PAGE_SIZE_A4, HPDF_PAGE_PORTRAIT);
            current_y = HPDF_Page_GetHeight(page) - 50;

            // 在新页面上右上角绘制北京时间
            HPDF_Page_BeginText(page);
            HPDF_Page_SetFontAndSize(page, timestamp_font, timestamp_font_size);
            HPDF_Page_TextOut(page, timestamp_x, timestamp_y, timestamp.c_str());
            HPDF_Page_EndText(page);

            // 在新页面上绘制右上角绘制 UNIX 时间戳
            HPDF_Page_BeginText(page);
            HPDF_Page_SetFontAndSize(page, info_font, info_font_size);
            HPDF_Page_TextOut(page, info_x, info_y, left_top_text.c_str());
            HPDF_Page_EndText(page);

            // 在新页面最下方的中间绘制页码
            HPDF_Page_BeginText(page);
            page_number_text = "Page " + to_string(page_number);
            page_number_x = HPDF_Page_GetWidth(page) / 2;
            page_number_y = 20;
            // NOTE: 经测试，页码为单位数时，鄙人认为这个参数 23.0 效果最好，双位数效果一般，但眼看花了，就暂时搁置了
            HPDF_Page_TextOut(page, page_number_x - 23.0, page_number_y, page_number_text.c_str());

            HPDF_Page_EndText(page);

            page_number++;
        }
    }

    // 保存并清理资源
    for (;;)
    {
        if (HPDF_SaveToFile(pdf, output_pdf_path.c_str()) == HPDF_OK)
        {
            cout << "PDF saved successfully" << '\n';
            // saveTerminalOutputToFile("PDF saved successfully", FILE_PATH);
            break;
        }
        else
        {
            cerr << "Failed to save PDF" << endl;
            // saveTerminalOutputToFile("Failed to save PDF", FILE_PATH);
        }
    }

    HPDF_Free(pdf);
    input_file.close();

    return true;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return EXIT_FAILURE;
    }

    for (int i = 1; i < argc; ++i)
    {
        fs::path input_path(argv[i]);

        // 判断文件扩展名是否为 .log
        if (input_path.extension() != ".log")
        {
            continue;
        }
        string output_pdf_path = input_path.replace_extension(".pdf").string();
        fromTextDocumentToPDF(string(argv[i]), output_pdf_path);
    }

    return EXIT_SUCCESS;
}