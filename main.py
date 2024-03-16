#!/home/m0rtzz/Program_Files/anaconda3/envs/py38/bin/python3

# ///////////////////////////////////////////////////////////////
#
# @file main.py
# @brief 程序入口文件
# @author M0rtzz E-mail: m0rtzz@163.com
# @version 4.0
# @PROJECT MADE WITH: Qt Designer and PySide6
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import subprocess
import cv2
import time
import pyautogui

# IMPORT / GUI AND MODULES AND WIDGETS
from modules import *
from widgets import *

from scripts.alipay import AlipayPayment

# NOTE: 禁止指定警告输出
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dark_theme_enabled = True
        self.file_names = set()
        self.file_paths = set()
        self.fisheye_directory = './images/my_images/fisheye_dataset'
        self.common_directory = './images/my_images/other_sensors'
        self.normal_directory = './images/my_images/fisheye_transformation/normal2fisheye'
        self.cubemap_directory = './images/my_images/fisheye_transformation/cubemap2fisheye'
        self.sem_seg_directory = './images/my_images/sem_seg/output'
        self.is_plus = False

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        title = "VisionVoyage - Modern GUI"
        # description = "VisionVoyage - 一款基于鱼眼相机与其他感知技术的自动驾驶仿真系统。"

        # # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)
        self.ui.line_edit_filenames.textChanged.connect(self.handleLineEditChange)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # BUTTON
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_image.clicked.connect(self.buttonClick)
        widgets.btn_simulation.clicked.connect(self.buttonClick)
        widgets.btn_personal_center.clicked.connect(self.buttonClick)
        widgets.btn_adjustments.clicked.connect(self.buttonClick)
        widgets.btn_my_image.clicked.connect(self.buttonClick)
        widgets.btn_open_dir.clicked.connect(self.buttonClick)
        widgets.btn_fisheye_one2one.clicked.connect(self.buttonClick)
        widgets.btn_fisheye_five2one.clicked.connect(self.buttonClick)
        widgets.btn_segmentation_image.clicked.connect(self.buttonClick)
        widgets.btn_segmentation_video.clicked.connect(self.buttonClick)
        widgets.btn_get_fisheye.clicked.connect(self.buttonClick)
        widgets.btn_get_common.clicked.connect(self.buttonClick)
        widgets.btn_raw_to_platte.clicked.connect(self.buttonClick)
        widgets.btn_start_server.clicked.connect(self.buttonClick)
        widgets.btn_generate_traffic.clicked.connect(self.buttonClick)
        widgets.btn_manual_control.clicked.connect(self.buttonClick)
        widgets.btn_automatic_control.clicked.connect(self.buttonClick)
        widgets.btn_send_mail.clicked.connect(self.buttonClick)
        widgets.btn_print.clicked.connect(self.buttonClick)
        widgets.btn_unlock.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.btn_personal_center.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        use_custom_theme = True
        # theme_file = "./themes/light.qss"
        theme_file = "./themes/dark.qss"

        # SET THEME AND HACKS
        if use_custom_theme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, theme_file, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    def setTableFontColor(self, table_widget):
        row_count = table_widget.rowCount()
        column_count = table_widget.columnCount()

        # 遍历所有单元格
        for row in range(row_count):
            for col in range(column_count):
                item = table_widget.item(row, col)
                if item is not None:
                    if self.dark_theme_enabled == True:  # 是黑色主题
                        color = QColor(255, 255, 255)  # 白色
                        item.setForeground(color)
                    else:
                        color = QColor(0, 0, 0)  # 黑色
                        item.setForeground(color)

    def clearColumn(self, widget, column_index):
        # 获取表格的行数
        row_count = widget.rowCount()

        # 清空指定列的每个单元格
        for row in range(row_count):
            item = widget.item(row, column_index)
            if item is not None:
                widget.takeItem(row, column_index)

    def onItemClickedSemSeg(self, item):
        column = item.column()
        row = item.row()
        table_widget = item.tableWidget()
        file_name = table_widget.item(row, column).text()
        # 遍历 output 目录下的所有子目录
        for root, dirs, files in os.walk(self.sem_seg_directory):
            for name in files:
                if name == file_name:
                    file_path = os.path.join(root, name)
                    if os.path.exists(file_path):
                        if file_name.endswith(".mp4"):
                            self.openVideoWithDefaultPlayer(file_path)
                        else:
                            cv2.namedWindow(file_name, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
                            cv2.resizeWindow(file_name, 800, 600)
                            mat = cv2.imread(file_path)
                            cv2.imshow(file_name, mat)
                        return
        print("File not found:", file_name)

    def onItemClickedFisheye(self, item):
        column = item.column()
        row = item.row()
        table_widget = item.tableWidget()
        file_name = table_widget.item(row, column).text()

        # 遍历 fisheye_dataset 目录下的所有子目录
        for root, dirs, files in os.walk(self.fisheye_directory):
            for name in files:
                if name == file_name:  # 如果找到了匹配的文件名
                    file_path = os.path.join(root, name)
                    if os.path.exists(file_path):  # 检查文件是否存在
                        cv2.namedWindow(file_name, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
                        cv2.resizeWindow(file_name, 800, 600)  # 设置窗口大小为 800x600
                        mat = cv2.imread(file_path)
                        cv2.imshow(file_name, mat)
                        return  # 找到文件后就返回，不再继续搜索
        print("File not found:", file_name)  # 如果没有找到文件，打印信息

    def onItemClickedCommon(self, item):
        column = item.column()
        row = item.row()
        table_widget = item.tableWidget()
        file_name = table_widget.item(row, column).text()

        for root, dirs, files in os.walk(self.common_directory):
            if file_name in files:
                file_path = os.path.join(root, file_name)
                cv2.namedWindow(file_name, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
                cv2.resizeWindow(file_name, 800, 600)  # 设置窗口大小为 800x600
                mat = cv2.imread(file_path)
                cv2.imshow(file_name, mat)

    def onItemClickedPT(self, item):
        column = item.column()
        row = item.row()
        table_widget = item.tableWidget()
        file_name = table_widget.item(row, column).text()
        file_path = os.path.join(self.normal_directory, file_name)
        if os.path.exists(file_path):  # 检查文件是否存在
            # file_dir = os.path.dirname(file_path)
            # self.openVisualDirectory(file_dir)  # 打开文件所在文件夹
            cv2.namedWindow(file_name, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
            cv2.resizeWindow(file_name, 800, 600)  # 设置窗口大小为 800x600
            mat = cv2.imread(file_path)
            cv2.imshow(file_name, mat)

    def onItemClickedCubemap(self, item):
        column = item.column()
        row = item.row()
        table_widget = item.tableWidget()
        file_name = table_widget.item(row, column).text()
        file_path = os.path.join(self.cubemap_directory, file_name)
        if os.path.exists(file_path):  # 检查文件是否存在
            # file_dir = os.path.dirname(file_path)
            # self.openVisualDirectory(file_dir)  # 打开文件所在文件夹
            cv2.namedWindow(file_name, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
            cv2.resizeWindow(file_name, 800, 600)  # 设置窗口大小为 800x600
            mat = cv2.imread(file_path)
            cv2.imshow(file_name, mat)

    def handleLineEditChange(self, text):
        if not text:  # 如果LineEdit内容为空
            self.file_names.clear()  # 清空file_names集合
            self.file_paths.clear()  # 清空file_paths集合

    def openVideoWithDefaultPlayer(self, video_path):
        if sys.platform.startswith('linux'):  # Linux
            subprocess.run(['xdg-open', video_path])
        elif sys.platform == 'darwin':  # MacOS
            subprocess.run(['open', video_path])
        elif sys.platform == 'win32':  # Windows
            subprocess.run(['start', '', video_path], shell=True)
        else:
            print("Unsupported operating system")

    def openVisualDirectory(self, directory):
        if sys.platform.startswith('linux'):  # Linux或类Unix系统
            os.system(f"xdg-open {directory}")
        elif sys.platform == 'darwin':  # macOS
            os.system(f"open {directory}")
        elif sys.platform == 'win32':  # Windows
            os.system(f"start {directory}")
        else:
            print("Unsupported platform")

    def openImage(self, folder_path, flag=False):
        # 检查文件夹路径是否存在
        if not os.path.isdir(folder_path):
            print("指定的文件夹不存在")
            return

        # 支持的图片格式列表
        image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']

        if not flag:  # 如果不需要查找最新更改的文件
            # 查找文件夹中第一张图片
            first_image = None
            for file in sorted(os.listdir(folder_path)):
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    first_image = file
                    break

            # 如果没有找到图片
            if not first_image:
                print("在指定的文件夹中没有找到图片")
                return

            # 获取完整的文件路径
            image_path = os.path.join(folder_path, first_image)
        else:  # 如果需要查找最新更改的文件
            # 查找文件夹中最新更改的图片
            latest_image = None
            latest_time = 0
            for file in sorted(os.listdir(folder_path)):
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    file_path = os.path.join(folder_path, file)
                    file_time = os.path.getmtime(file_path)
                    if file_time > latest_time:
                        latest_time = file_time
                        latest_image = file

            # 如果没有找到图片
            if not latest_image:
                print("在指定的文件夹中没有找到图片")
                return

            # 获取完整的文件路径
            image_path = os.path.join(folder_path, latest_image)

        # 根据不同的操作系统打开图片
        try:
            if sys.platform.startswith('win32'):  # Windows
                os.startfile(image_path)
            elif sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', image_path])
            else:  # Linux或类Unix系统
                subprocess.run(['xdg-open', image_path])
        except Exception as e:
            print(f"打开图片时出现错误: {e}")

    def becomePlus(self):
        app_private_key_path = "./certs/app_private_key.pem"
        alipay_public_key_path = "./certs/alipay_public_key.pem"
        background_url = 'https://jsd.cdn.zzko.cn/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:03/Day:15/22:26:14_background.png'

        alipay_payment = AlipayPayment(app_private_key_path, alipay_public_key_path)
        qr_code_url, out_trade_no_with_time = alipay_payment.createOrder()
        qr_cv = alipay_payment.generateQrCode(qr_code_url)
        alipay_payment.displayQrCodeOnBackground(qr_cv, background_url)

        # 检查支付状态
        self.is_plus = alipay_payment.checkPaymentStatus(out_trade_no_with_time)

    def close_window_by_title(self, window_title):
        if sys.platform.startswith('win32'):  # Windows
            command = f'taskkill /F /FI "WINDOWTITLE eq {window_title}"'
            os.system(command)
        elif sys.platform.startswith('darwin'):  # macOS
            command = f"osascript -e 'quit app \"{window_title}\"'"
            os.system(command)
        elif sys.platform.startswith('linux'):  # Linux或类Unix系统
            command = f'wmctrl -c "{window_title}"'
            os.system(command)
        else:
            print("Unsupported platform")

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btn_name = btn.objectName()

        if btn_name == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btn_name == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btn_name == "btn_image":
            while True:
                if self.is_plus:
                    break
                else:
                    self.becomePlus()
                    self.close_window_by_title("请在三分钟内完成支付")
                    time.sleep(2)
            widgets.stackedWidget.setCurrentWidget(widgets.image_page)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btn_name == "btn_simulation":
            while True:
                if self.is_plus:
                    break
                else:
                    self.becomePlus()
                    self.close_window_by_title("请在三分钟内完成支付")
                    time.sleep(2)
            widgets.stackedWidget.setCurrentWidget(widgets.simulation_page)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btn_name == "btn_my_image":
            # os.system("nautilus ./images/my_images")
            self.openVisualDirectory("./images/my_images")

        elif btn_name == "btn_open_dir":
            # 点击按钮自动清空 self.ui.line_edit_filenames 和 self.file_paths
            self.ui.line_edit_filenames.clear()
            self.file_paths.clear()
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)  # 设置多选模式
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog  # 禁用原生对话框
            # files, _ = file_dialog.getOpenFileNames(self, "选择文件", "", "所有文件 (*)")
            filter = "图像文件 (*.png *.jpg *.bmp *.jpeg);;视频文件 (*.mp4 *.avi *.mov *.mkv)"
            files, _ = file_dialog.getOpenFileNames(
                None, "选择图片或视频", "./images/my_images", filter, options=options)
            if files:
                self.file_names.update([os.path.basename(file) for file in files])  # 将已选择的文件名添加到集合中
                self.ui.line_edit_filenames.setText(", ".join(self.file_names))
                self.file_paths.update([os.path.relpath(file, "./")
                                       for file in files])  # 将已选择的文件的相对路径添加到集合中

        elif btn_name == "btn_fisheye_one2one":
            # terminal_command = "./scripts/PT2fisheye.py " + " ".join(self.file_paths)
            terminal_command = "./scripts/PT2fisheye.out " + " ".join(self.file_paths)
            os.system(terminal_command)
            directory = './images/my_images/fisheye_transformation/normal2fisheye'
            table_widget = widgets.table_widget_transform_upload_result

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedPT)
            # 获取目录中的所有.png文件
            png_files = [file for file in os.listdir(directory) if file.endswith(".png")]

            # 清空第一列的内容
            self.clearColumn(table_widget, 0)

            # 在第一列的每一行中显示文件名
            for index, file in enumerate(png_files):
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 0, item)

            self.openImage('./images/my_images/fisheye_transformation/normal2fisheye', flag=True)

        elif btn_name == "btn_fisheye_five2one":
            # terminal_command = "./scripts/cubemap2fisheye.py " + " ".join(self.file_paths)
            terminal_command = "./scripts/cubemap2fisheye.out " + " ".join(self.file_paths)
            os.system(terminal_command)
            directory = './images/my_images/fisheye_transformation/cubemap2fisheye'
            table_widget = widgets.table_widget_transform_upload_result

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedCubemap)
            # 获取目录中的所有.png文件
            png_files = [file for file in os.listdir(directory) if file.endswith(".png")]

            # 清空第二列的内容
            self.clearColumn(table_widget, 1)

            # 在第二列的每一行中显示文件名
            for index, file in enumerate(png_files):
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 1, item)

            self.openImage('./images/my_images/fisheye_transformation/cubemap2fisheye', flag=True)

        elif btn_name == "btn_segmentation_image":
            terminal_command = "./scripts/sem_seg_image.py --image_paths " + " ".join(self.file_paths)
            os.system(terminal_command)
            base_directory = './images/my_images/sem_seg/output'
            table_widget = widgets.table_widget_transform_upload_result

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedSemSeg)

            # 指定要查找.png文件的子目录列表
            sub_dirs = ['images', 'videos']

            # 获取指定子目录中的所有.png和.mp4文件
            media_files = []
            for sub_dir in sub_dirs:
                dir_path = os.path.join(base_directory, sub_dir)
                if os.path.exists(dir_path):
                    media_files.extend([os.path.join(sub_dir, file)
                                        for file in os.listdir(dir_path) if file.endswith(".png") or file.endswith(".mp4")])

            # 清空第三列的内容
            self.clearColumn(table_widget, 2)

            # 在表格中显示文件名，去掉路径，只显示文件名
            for index, file in enumerate(media_files):
                # 使用os.path.basename去掉路径，只保留文件名
                file = os.path.basename(file)
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 2, item)

        elif btn_name == "btn_segmentation_video":
            terminal_command = "./scripts/sem_seg_video.py --weights ./scripts/weights/video.pt --source " + \
                " ".join(self.file_paths)
            os.system(terminal_command)
            base_directory = './images/my_images/sem_seg/output'
            table_widget = widgets.table_widget_transform_upload_result

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedSemSeg)

            # 指定要查找.png文件的子目录列表
            sub_dirs = ['images', 'videos']

            # 获取指定子目录中的所有.png和.mp4文件
            media_files = []
            for sub_dir in sub_dirs:
                dir_path = os.path.join(base_directory, sub_dir)
                if os.path.exists(dir_path):
                    media_files.extend([os.path.join(sub_dir, file)
                                        for file in os.listdir(dir_path) if file.endswith(".png") or file.endswith(".mp4")])

            # 清空第三列的内容
            self.clearColumn(table_widget, 2)

            # 在表格中显示文件名，去掉路径，只显示文件名
            for index, file in enumerate(media_files):
                # 使用os.path.basename去掉路径，只保留文件名
                file = os.path.basename(file)
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 2, item)

        elif btn_name == "btn_raw_to_platte":
            os.system("./scripts/change_index.out")
            os.system("./scripts/gray2color.out")
            self.openImage('./images/my_images/fisheye_dataset/semantic_segmentation_CityScapesPalette')

        elif btn_name == "btn_start_server":
            subprocess.Popen(['gnome-terminal', '--title', 'VisionVoyage Server状态终端',
                             '--', 'sh', './scripts/VisionVoyageServer.sh', "-quality-level=low"])

        elif btn_name == "btn_generate_traffic":
            subprocess.Popen(['gnome-terminal', '--title', '交通初始化',
                             '--', './scripts/generate_traffic.py'])

        elif btn_name == "btn_manual_control":
            subprocess.Popen(['gnome-terminal', '--title', '虚拟驾驶',
                              '--', './scripts/manual_control.py'])

        elif btn_name == "btn_automatic_control":
            subprocess.Popen(['gnome-terminal', '--title', '自动驾驶',
                              '--', './scripts/automatic_control.py'])

        elif btn_name == "btn_get_fisheye":
            os.system("./scripts/dataset_main.py")
            base_directory = './images/my_images/fisheye_dataset'
            table_widget = widgets.table_widget_get_image

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedFisheye)

            # 指定要查找.png文件的子目录列表
            sub_dirs = ['rgb', 'semantic_segmentation_raw', 'semantic_segmentation_CityScapesPalette']

            # 获取指定子目录中的所有.png文件
            png_files = []
            for sub_dir in sub_dirs:
                dir_path = os.path.join(base_directory, sub_dir)
                if os.path.exists(dir_path):
                    png_files.extend([os.path.join(sub_dir, file)
                                      for file in os.listdir(dir_path) if file.endswith(".png")])

            # 清空第一列的内容
            self.clearColumn(table_widget, 0)

            # 在表格中显示文件名，去掉路径，只显示文件名
            for index, file in enumerate(png_files):
                # 使用os.path.basename去掉路径，只保留文件名
                file = os.path.basename(file)
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 0, item)

        elif btn_name == "btn_get_common":
            os.system("./scripts/manual_control_gbuffer.py")
            directory = './images/my_images/other_sensors'
            table_widget = widgets.table_widget_get_image

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedCommon)

            # 获取目录中的所有.png文件
            # png_files = [file for file in os.listdir(directory) if file.endswith(".png")]
            png_files = [os.path.basename(os.path.join(dp, f)) for dp, dn, filenames in os.walk(directory)
                         for f in filenames if f.endswith(".png")]

            # 清空第二列的内容
            self.clearColumn(table_widget, 1)

            # 在第二列的每一行中显示文件名
            for index, file in enumerate(png_files):
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 1, item)

        elif btn_name == "btn_adjustments":
            self.dark_theme_enabled = not self.dark_theme_enabled

            # 根据当前主题选择相应的主题文件
            if self.dark_theme_enabled:
                theme_file = "./themes/dark.qss"
                # 设置字体为颜色为白色
                widgets.btn_fisheye_one2one.setStyleSheet("color: #FFFFFF;")
                widgets.btn_fisheye_five2one.setStyleSheet("color: #FFFFFF;")
                widgets.btn_segmentation_image.setStyleSheet("color: #FFFFFF;")
                widgets.btn_segmentation_video.setStyleSheet("color: #FFFFFF;")
                widgets.btn_get_fisheye.setStyleSheet("color: #FFFFFF;")
                widgets.btn_get_common.setStyleSheet("color: #FFFFFF;")
                widgets.btn_raw_to_platte.setStyleSheet("color: #FFFFFF;")
                widgets.btn_generate_traffic.setStyleSheet("color: #FFFFFF;")
                widgets.btn_manual_control.setStyleSheet("color: #FFFFFF;")
                widgets.btn_automatic_control.setStyleSheet("color: #FFFFFF;")
                widgets.line_edit_operation_help.setStyleSheet("color: #FFFFFF;")
                # widgets.table_widget_get_image.setStyleSheet("color: #FFFFFF;")
                self.setTableFontColor(widgets.table_widget_get_image)
                self.setTableFontColor(widgets.table_widget_operation_help)

            else:
                theme_file = "./themes/light.qss"
                # 设置字体为颜色为黑色
                widgets.btn_fisheye_one2one.setStyleSheet("color: #000000;")
                widgets.btn_fisheye_five2one.setStyleSheet("color: #000000;")
                widgets.btn_segmentation_image.setStyleSheet("color: #000000;")
                widgets.btn_segmentation_video.setStyleSheet("color: #000000;")
                widgets.btn_get_fisheye.setStyleSheet("color: #000000;")
                widgets.btn_get_common.setStyleSheet("color: #000000;")
                widgets.btn_raw_to_platte.setStyleSheet("color: #000000;")
                widgets.btn_raw_to_platte.setStyleSheet("color: #000000;")
                widgets.btn_generate_traffic.setStyleSheet("color: #000000;")
                widgets.btn_manual_control.setStyleSheet("color: #000000;")
                widgets.btn_automatic_control.setStyleSheet("color: #000000;")
                widgets.line_edit_operation_help.setStyleSheet("color: #000000;")
                # widgets.table_widget_get_image.setStyleSheet("color: #000000;")
                self.setTableFontColor(widgets.table_widget_get_image)
                self.setTableFontColor(widgets.table_widget_operation_help)
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, theme_file, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

        elif btn_name == "btn_send_mail":
            import webbrowser
            to_email = "m0rtzz@outlook.com"
            webbrowser.open("mailto:" + to_email, new=1)

        elif btn_name == "btn_print":
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)  # 设置多选模式
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog  # 禁用原生对话框
            # files, _ = file_dialog.getOpenFileNames(self, "选择文件", "", "所有文件 (*)")
            filter = "文件 (*.txt *.pdf)"
            files, _ = file_dialog.getOpenFileNames(
                None, "选择文本或PDF文件", "./logs", filter, options=options)
            terminal_command_1 = "./scripts/txt2pdf.out " + " ".join(files)
            os.system(terminal_command_1)
            print_files = set(file.replace(".txt", ".pdf") if file.endswith(
                ".txt") else file.replace(".pdf", ".pdf") for file in files)
            terminal_command_2 = "pdftk " + " ".join(print_files) + " cat output - | lpr"
            os.system(terminal_command_2)

        elif btn_name == "btn_unlock":
            self.becomePlus()

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
