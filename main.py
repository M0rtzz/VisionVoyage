# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

from enum import auto
import sys
import os
import platform
import subprocess
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import imread
import cv2

# IMPORT / GUI AND MODULES AND WIDGETS
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dark_theme_enabled = True
        self.file_names = set()
        self.file_paths = set()
        self.fisheye_directory = 'images/my_images/fisheye_dataset'
        self.common_directory = 'images/my_images/other_sensors'

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
        # theme_file = "./themes/py_dracula_light.qss"
        theme_file = "./themes/py_dracula_dark.qss"

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
        file_path = os.path.join(self.common_directory, file_name)
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

    def openVisualDirectory(self, directory):
        if sys.platform.startswith('linux'):  # Linux
            os.system(f"xdg-open {directory}")
        elif sys.platform == 'darwin':  # macOS
            os.system(f"open {directory}")
        elif sys.platform == 'win32':  # Windows
            os.system(f"start {directory}")
        else:
            print("Unsupported platform")

    def openFirstImage(self, folder_path):
        # 检查文件夹路径是否存在
        if not os.path.isdir(folder_path):
            print("指定的文件夹不存在")
            return

        # 支持的图片格式列表
        image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']

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

        # 根据不同的操作系统打开图片
        try:
            if sys.platform.startswith('win32'):
                os.startfile(image_path)  # Windows
            elif sys.platform.startswith('darwin'):
                subprocess.run(['open', image_path])  # macOS
            else:  # 假设是Linux或类Unix系统
                subprocess.run(['xdg-open', image_path])
        except Exception as e:
            print(f"打开图片时出现错误: {e}")

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
            widgets.stackedWidget.setCurrentWidget(widgets.image_page)  # SET PAGE
            UIFunctions.resetStyle(self, btn_name)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        elif btn_name == "btn_simulation":
            widgets.stackedWidget.setCurrentWidget(widgets.simulation_page)  # SET PAGE
            UIFunctions.resetStyle(self, btn_name)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        elif btn_name == "btn_personal_center":
            print("btn_personal_center clicked!")

        elif btn_name == "btn_my_image":
            print("btn_my_image clicked!")
            # os.system("nautilus ./images/my_images")
            self.openVisualDirectory("./images/my_images")

        elif btn_name == "btn_open_dir":
            print("btn_open_dir clicked!")
            print("self.file_names", self.file_names)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)  # 设置多选模式
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog  # 禁用原生对话框
            # files, _ = file_dialog.getOpenFileNames(self, "选择文件", "", "所有文件 (*)")
            files, _ = file_dialog.getOpenFileNames(
                None, "选择图片", "./images/my_images", "图像文件 (*.png *.jpg *.bmp *.jpeg)", options=options)
            if files:
                self.file_names.update([os.path.basename(file) for file in files])  # 将已选择的文件名添加到集合中
                self.ui.line_edit_filenames.setText(", ".join(self.file_names))
                self.file_paths.update([os.path.relpath(file, "./")
                                       for file in files])  # 将已选择的文件的相对路径添加到集合中

        elif btn_name == "btn_fisheye_one2one":
            print("btn_fisheye_one2one clicked!")
            terminal_command = "./scripts/PT2fisheye.py " + " ".join(self.file_paths)
            os.system(terminal_command)
            self.openFirstImage('./images/my_images/fisheye_transformation/normal2fisheye')

        elif btn_name == "btn_fisheye_five2one":
            print("btn_fisheye_five2one clicked!")
            terminal_command = "./scripts/cubemap2fisheye.py " + " ".join(self.file_paths)
            os.system(terminal_command)

        elif btn_name == "btn_segmentation_image":
            print("btn_segmentation_image clicked!")

        elif btn_name == "btn_segmentation_video":
            print("btn_segmentation_video clicked!")

        elif btn_name == "btn_raw_to_platte":
            print("btn_raw_to_platte clicked!")
            os.system("./scripts/gray2color")
            self.openFirstImage('./images/my_images/fisheye_dataset/semantic_segmentation_CityScapesPalette')

        elif btn_name == "btn_start_server":
            print("btn_start_server clicked!")
            subprocess.Popen(['gnome-terminal', '--title', 'VisionVoyage Server启动终端',
                             '--', 'sh', './scripts/VisionVoyageServer.sh'])

        elif btn_name == "btn_generate_traffic":
            print("btn_generate_traffic clicked!")
            subprocess.Popen(['gnome-terminal', '--title', '交通初始化',
                             '--', 'python3', './scripts/generate_traffic.py'])

        elif btn_name == "btn_manual_control":
            print("btn_manual_control clicked!")
            subprocess.Popen(['gnome-terminal', '--title', '虚拟驾驶',
                              '--', 'python3', './scripts/manual_control.py'])

        elif btn_name == "btn_automatic_control":
            print("btn_automatic_control clicked!")
            subprocess.Popen(['gnome-terminal', '--title', '自动驾驶',
                              '--', 'python3', './scripts/automatic_control.py'])

        elif btn_name == "btn_get_fisheye":
            print("btn_get_fisheye clicked!")
            base_directory = './images/my_images/fisheye_dataset'
            table_widget = widgets.table_widget_get_image

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedFisheye)

            # 指定要查找.png文件的子目录列表
            sub_dirs = ['rgb', 'semantic_segmentation_raw']

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
            print("btn_get_common clicked!")
            directory = './images/my_images/other_sensors'
            table_widget = widgets.table_widget_get_image

            # 连接itemClicked信号到槽函数
            table_widget.itemClicked.connect(self.onItemClickedCommon)
            # 获取目录中的所有.png文件
            png_files = [file for file in os.listdir(directory) if file.endswith(".png")]

            # 清空第二列的内容
            self.clearColumn(table_widget, 1)

            # 在第二列的每一行中显示文件名
            for index, file in enumerate(png_files):
                item = QTableWidgetItem(file)
                table_widget.setItem(index, 1, item)

        elif btn_name == "btn_adjustments":
            print("btn_adjustments clicked!")
            self.dark_theme_enabled = not self.dark_theme_enabled

            # 根据当前主题选择相应的主题文件
            if self.dark_theme_enabled:
                theme_file = "./themes/py_dracula_dark.qss"
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
                theme_file = "./themes/py_dracula_light.qss"
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

        # PRINT BTN NAME
        print(f'Button "{btn_name}" pressed!')

    # RESIZE EVENTS

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
