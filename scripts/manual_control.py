#!/home/m0rtzz/Program_Files/anaconda3/envs/py38/bin/python3

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

# Allows controlling a vehicle with a keyboard. For a simpler and more
# documented example, please take a look at tutorial.py.

                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)

                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
#     S            : brake
                               QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
                               QVBoxLayout, QWidget)
#     M            : toggle manual transmission

#     ,/.          : gear up/down
#     CTRL + W     : toggle constant velocity mode at 60 km/h

#     L            : toggle next light type
#     SHIFT + L    : toggle high beam
#     Z/X          : toggle right/left blinker
#     I            : toggle interior light

#     TAB          : change sensor position
#     ` or N       : next sensor
#     [1-9]        : change to sensor [1-9]
#     G            : toggle radar visualization
#     C            : change weather (Shift+C reverse)
#     Backspace    : change vehicle

#     O            : open/close all doors of vehicle
#     T            : toggle vehicle's telemetry

#     V            : Select next map layer (Shift+V reverse)
                                      "\n"
                                      "SET APP STYLESHEET - FULL STYLES HERE\n"
                                      "DARK THEME - DRACULA COLOR BASED\n"
                                      "\n"
                                      "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
                                      "\n"
                                      "QWidget{\n"
                                      "	color: rgb(221, 221, 221);\n"
                                      "	font: 10pt \"Segoe UI\";\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Tooltip */\n"
                                      "QToolTip {\n"
                                      "	color: #ffffff;\n"
                                      "	background-color: rgba(33, 37, 43, 180);\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "	background-image: none;\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 2px solid rgb(255, 121, 198);\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 8px;\n"
                                      "	margin: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Bg App */\n"
                                      "#bgApp {	\n"
                                      "	background"
                                      "-color: rgb(40, 44, 52);\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Left Menu */\n"
                                      "#leftMenuBg {	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "#topLogo {\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	background-image: url(:/images/images/images/VisionVoyage.png);\n"
                                      "	background-position: centered;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "}\n"
                                      "#titleLeftApp { font: 8pt \"Segoe UI\"; }\n"
                                      "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
                                      "\n"
                                      "/* MENUS */\n"
                                      "#topMenu .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color: transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#topMenu .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#topMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 24"
                                      "9);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 20px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#leftMenuFrame{\n"
                                      "	border-top: 3px solid rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "/* Toggle Button */\n"
                                      "#toggleButton {\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 20px solid transparent;\n"
                                      "	background-color: rgb(37, 41, 48);\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "	color: rgb(113, 126, 149);\n"
                                      "}\n"
                                      "#toggleButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#toggleButton:pressed {\n"
                                      "	background-color: rgb(189, 147, "
                                      "249);\n"
                                      "}\n"
                                      "\n"
                                      "/* Title Menu */\n"
                                      "#titleRightInfo { padding-left: 10px; }\n"
                                      "\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Extra Tab */\n"
                                      "#extraLeftBox {	\n"
                                      "	background-color: rgb(44, 49, 58);\n"
                                      "}\n"
                                      "#extraTopBg{	\n"
                                      "	background-color: rgb(189, 147, 249)\n"
                                      "}\n"
                                      "\n"
                                      "/* Icon */\n"
                                      "#extraIcon {\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	\n"
                                      "}\n"
                                      "\n"
                                      "/* Label */\n"
                                      "#extraLabel { color: rgb(255, 255, 255); }\n"
                                      "\n"
                                      "/* Btn Close */\n"
                                      "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                      "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
                                      "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
                                      "\n"
                                      "/* Extra Content */\n"
                                      "#extraContent{\n"
                                      "	border-top: 3px solid rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "/* Extra Top Menus */\n"
                                      ""
                                      "#extraTopMenu .QPushButton {\n"
                                      "background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#extraTopMenu .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#extraTopMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Content App */\n"
                                      "#contentTopBg{	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "#contentBottom{\n"
                                      "	border-top: 3px solid rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "/* Top Buttons */\n"
                                      "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                      "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
                                      "#rightButtons .QPushButton:pressed { "
                                      "background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
                                      "\n"
                                      "/* Theme Settings */\n"
                                      "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
                                      "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
                                      "\n"
                                      "/* Bottom Bar */\n"
                                      "#bottomBar { background-color: rgb(44, 49, 58); }\n"
                                      "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
                                      "\n"
                                      "/* CONTENT SETTINGS */\n"
                                      "/* MENUS */\n"
                                      "#contentSettings .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#contentSettings .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#contentSettings .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* ///////////////////////////////////////"
                                      "//////////////////////////////////////////////////////////\n"
                                      "QTableWidget */\n"
                                      "QTableWidget {	\n"
                                      "	background-color: transparent;\n"
                                      "	padding: 10px;\n"
                                      "	border-radius: 5px;\n"
                                      "	gridline-color: rgb(44, 49, 58);\n"
                                      "	border-bottom: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::item{\n"
                                      "	border-color: rgb(44, 49, 60);\n"
                                      "	padding-left: 5px;\n"
                                      "	padding-right: 5px;\n"
                                      "	gridline-color: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::item:selected{\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "}\n"
                                      "QHeaderView::section{\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	max-width: 30px;\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "	border-style: none;\n"
                                      "    border-bottom: 1px solid rgb(44, 49, 60);\n"
                                      "    border-right: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::horizontalHeader {	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "QHeaderView::section:horizontal\n"
                                      "{\n"
                                      "    border: 1px solid rgb(33, 37, 43);\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	padding: 3px;\n"
                                      "	border-top-left-radius: 7px;"
                                      "\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "}\n"
                                      "QHeaderView::section:vertical\n"
                                      "{\n"
                                      "    border: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "LineEdit */\n"
                                      "QLineEdit {\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(33, 37, 43);\n"
                                      "	padding-left: 10px;\n"
                                      "	selection-color: rgb(255, 255, 255);\n"
                                      "	selection-background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "PlainTextEdit */\n"
                                      "QPlainTextEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	padding: 10px;\n"
                                      "	selection-color: rgb(255, 255, 255);\n"
                                      "	selection-background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "QPlainTextEdit  QScrollBar:vertical {\n"
                                      ""
                                      "    width: 8px;\n"
                                      " }\n"
                                      "QPlainTextEdit  QScrollBar:horizontal {\n"
                                      "    height: 8px;\n"
                                      " }\n"
                                      "QPlainTextEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QPlainTextEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "ScrollBars */\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 8px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    background: rgb(189, 147, 249);\n"
                                      "    min-width: 25px;\n"
                                      "	border-radius: 4px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-right-radius: 4px;\n"
                                      "    border-bottom-right-radius: 4px;\n"
                                      "    subcontrol-position: right;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: "
                                      "rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "    border-bottom-left-radius: 4px;\n"
                                      "    subcontrol-position: left;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 8px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(189, 147, 249);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 4px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "     border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-bottom-left-radius: 4px;\n"
                                      "    border-bottom-right-radius: 4px;\n"
                                      "     subcontrol-position: bottom;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-line:vertical {\n"
                                      "	bo"
                                      "rder: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "    border-top-right-radius: 4px;\n"
                                      "     subcontrol-position: top;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "CheckBox */\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    background: 3px solid rgb(52, 59, 72);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/*"
                                      " /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "RadioButton */\n"
                                      "QRadioButton::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "    background: 3px solid rgb(94, 106, 130);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "ComboBox */\n"
                                      "QComboBox{\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(33, 37, 43);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      ""
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb(255, 121, 198);	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Sliders */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border-radius: 5px;\n"
                                      "    height: 10px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:horizontal:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background-color: rgb(189, 147, 249);\n"
                                      "    border: none;\n"
                                      "    height: 10px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 5px;"
                                      "\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "    background-color: rgb(195, 155, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "    background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border-radius: 5px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:vertical {\n"
                                      "    background-color: rgb(189, 147, 249);\n"
                                      "	border: none;\n"
                                      "    height: 10px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "    background-color: rgb(195, 155, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "    background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "CommandLinkButton */\n"
                                      "QCommandLinkButton {	\n"
                                      "	color: rgb(255, 121, 198);\n"
                                      "	border-radius: 5px;\n"
                                      "	paddi"
                                      "ng: 5px;\n"
                                      "	color: rgb(255, 170, 255);\n"
                                      "}\n"
                                      "QCommandLinkButton:hover {	\n"
                                      "	color: rgb(255, 170, 255);\n"
                                      "	background-color: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCommandLinkButton:pressed {	\n"
                                      "	color: rgb(189, 147, 249);\n"
                                      "	background-color: rgb(52, 58, 71);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Button */\n"
                                      "#pagesContainer QPushButton {\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	border-radius: 5px;	\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "#pagesContainer QPushButton:hover {\n"
                                      "	background-color: rgb(57, 65, 80);\n"
                                      "	border: 2px solid rgb(61, 70, 86);\n"
                                      "}\n"
                                      "#pagesContainer QPushButton:pressed {	\n"
                                      "	background-color: rgb(35, 40, 49);\n"
                                      "	border: 2px solid rgb(43, 50, 61);\n"
                                      "}\n"
                                      "\n"
                                      "")
                        self._control.manual_gear_shift = not self._control.manual_gear_shift
                        self._control.gear = world.player.get_control().gear
                        world.hud.notification('%s Transmission' %
                                               ('Manual' if self._control.manual_gear_shift else 'Automatic'))
                    elif self._control.manual_gear_shift and event.key == K_COMMA:
                        self._control.gear = max(-1, self._control.gear - 1)
                    elif self._control.manual_gear_shift and event.key == K_PERIOD:
                        self._control.gear = self._control.gear + 1
                    elif event.key == K_p and not pygame.key.get_mods() & KMOD_CTRL:
                        if not self._autopilot_enabled and not sync_mode:
                            print("WARNING: You are currently in asynchronous mode and could "
                                  "experience some issues with the traffic simulation")
                        self._autopilot_enabled = not self._autopilot_enabled
                        world.player.set_autopilot(self._autopilot_enabled)
                        world.hud.notification(
                            'Autopilot %s' % ('On' if self._autopilot_enabled else 'Off'))
                    elif event.key == K_l and pygame.key.get_mods() & KMOD_CTRL:
                        current_lights ^= carla.VehicleLightState.Special1
                    elif event.key == K_l and pygame.key.get_mods() & KMOD_SHIFT:
                        current_lights ^= carla.VehicleLightState.HighBeam
                    elif event.key == K_l:
                        # Use 'L' key to switch between lights:
                        # closed -> position -> low beam -> fog
                        if not self._lights & carla.VehicleLightState.Position:
                            world.hud.notification("Position lights")
                            current_lights |= carla.VehicleLightState.Position
                        else:
                            world.hud.notification("Low beam lights")
                            current_lights |= carla.VehicleLightState.LowBeam
                        if self._lights & carla.VehicleLightState.LowBeam:
                            world.hud.notification("Fog lights")
                            current_lights |= carla.VehicleLightState.Fog
                        if self._lights & carla.VehicleLightState.Fog:
                            world.hud.notification("Lights off")
                            current_lights ^= carla.VehicleLightState.Position
                            current_lights ^= carla.VehicleLightState.LowBeam
                            current_lights ^= carla.VehicleLightState.Fog
                    elif event.key == K_i:
                        current_lights ^= carla.VehicleLightState.Interior
                    elif event.key == K_z:
                        current_lights ^= carla.VehicleLightState.LeftBlinker
                    elif event.key == K_x:
                        current_lights ^= carla.VehicleLightState.RightBlinker

        if not self._autopilot_enabled:
        self.titleLeftApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
                self._parse_vehicle_keys(pygame.key.get_pressed(), clock.get_time())
                self._control.reverse = self._control.gear < 0
                # Set automatic control-related vehicle lights
                if self._control.brake:
                    current_lights |= carla.VehicleLightState.Brake
        self.titleLeftDescription.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
                    current_lights &= ~carla.VehicleLightState.Brake
                if self._control.reverse:
                    current_lights |= carla.VehicleLightState.Reverse
                else:  # Remove the Reverse flag
                    current_lights &= ~carla.VehicleLightState.Reverse
                if current_lights != self._lights:  # Change the light state only if necessary
                    self._lights = current_lights
                    world.player.set_light_state(carla.VehicleLightState(self._lights))
                # Apply control
                if not self._ackermann_enabled:
                    world.player.apply_control(self._control)
                else:
                    world.player.apply_ackermann_control(self._ackermann_control)
                    # Update control to the last one applied by the ackermann controller.
                    self._control = world.player.get_control()
                    # Update hud with the newest ackermann control
                    world.hud.update_ackermann_control(self._ackermann_control)

            elif isinstance(self._control, carla.WalkerControl):
                self._parse_walker_keys(pygame.key.get_pressed(), clock.get_time(), world)
                world.player.apply_control(self._control)

    def _parse_vehicle_keys(self, keys, milliseconds):
        if keys[K_UP] or keys[K_w]:
            if not self._ackermann_enabled:
                self._control.throttle = min(self._control.throttle + 0.01, 1.00)
            else:
                self._ackermann_control.speed += round(milliseconds * 0.005, 2) * self._ackermann_reverse
        else:
            if not self._ackermann_enabled:
                self._control.throttle = 0.0

        if keys[K_DOWN] or keys[K_s]:
            if not self._ackermann_enabled:
                self._control.brake = min(self._control.brake + 0.2, 1)
                self._ackermann_control.speed -= min(abs(self._ackermann_control.speed),
                                                     round(milliseconds * 0.005, 2)) * self._ackermann_reverse
                self._ackermann_control.speed = max(0, abs(self._ackermann_control.speed)) * self._ackermann_reverse
        else:
            if not self._ackermann_enabled:
                self._control.brake = 0

        steer_increment = 5e-4 * milliseconds
        if keys[K_LEFT] or keys[K_a]:
            if self._steer_cache > 0:
                self._steer_cache = 0
            else:
                self._steer_cache -= steer_increment
        elif keys[K_RIGHT] or keys[K_d]:
            if self._steer_cache < 0:
                self._steer_cache = 0
            else:
                self._steer_cache += steer_increment
        else:
            self._steer_cache = 0.0
        self._steer_cache = min(0.7, max(-0.7, self._steer_cache))
        if not self._ackermann_enabled:
            self._control.steer = round(self._steer_cache, 1)
            self._control.hand_brake = keys[K_SPACE]
        else:
            self._ackermann_control.steer = round(self._steer_cache, 1)

    def _parse_walker_keys(self, keys, milliseconds, world):
        self._control.speed = 0.0
        if keys[K_DOWN] or keys[K_s]:
            self._control.speed = 0.0
        if keys[K_LEFT] or keys[K_a]:
            self._control.speed = .01
            self._rotation.yaw -= 0.08 * milliseconds
        if keys[K_RIGHT] or keys[K_d]:
            self._control.speed = .01
            self._rotation.yaw += 0.08 * milliseconds
        if keys[K_UP] or keys[K_w]:
            self._control.speed = world.player_max_speed_fast if pygame.key.get_mods() & KMOD_SHIFT else world.player_max_speed
        self._control.jump = keys[K_SPACE]
        self._rotation.yaw = round(self._rotation.yaw, 1)
        self._control.direction = self._rotation.get_forward_vector()

    @staticmethod
    def _is_quit_shortcut(key):
        return (key == K_ESCAPE) or (key == K_q and pygame.key.get_mods() & KMOD_CTRL)


# ==============================================================================
# -- HUD -----------------------------------------------------------------------
# ==============================================================================


class HUD(object):
    # def __init__(self, width, height):
    #     self.dim = (width, height)
    #     font = pygame.font.Font(pygame.font.get_default_font(), 20)
    #     font_name = 'courier' if os.name == 'nt' else 'mono'
    #     default_font = 'ubuntumono'
    #     mono = default_font if default_font in fonts else fonts[0]
    #     mono = pygame.font.match_font(mono)
    #     self._font_mono = pygame.font.Font(mono, 12 if os.name == 'nt' else 14)
    #     self._notifications = FadingText(font, (width, 40), (0, height - 40))
    #     self.help = HelpText(pygame.font.Font(mono, 16), width, height)
    #     self.server_fps = 0
    #     self.frame = 0
    #     self.simulation_time = 0
    #     self._show_info = True
    #     self._info_text = []
    #     self._server_clock = pygame.time.Clock()

    #     self._show_ackermann_info = False
    #     self._ackermann_control = carla.VehicleAckermannControl()

    def __init__(self, width, height):
        self.dim = (width, height)
        # 使用本地黑体字体文件创建字体对象
        font_path = '/home/m0rtzz/Workspaces/VisionVoyage/Project/fonts/simhei.ttf'
        font_size = 20
        font = pygame.font.Font(font_path, font_size)
        self._font_mono = pygame.font.Font(font_path, 12 if os.name == 'nt' else 14)
        self._notifications = FadingText(font, (width, 40), (0, height - 40))
        help_font_size = 24
        self.server_fps = 0
        self.frame = 0
        self.simulation_time = 0
        self._show_info = True
        self._info_text = []
        self._server_clock = pygame.time.Clock()

        self._show_ackermann_info = False
        self._ackermann_control = carla.VehicleAckermannControl()

    def on_world_tick(self, timestamp):
        self._server_clock.tick()
        self.server_fps = self._server_clock.get_fps()
        self.frame = timestamp.frame
        self.simulation_time = timestamp.elapsed_seconds

    def tick(self, world, clock):
        self._notifications.tick(world, clock)
        if not self._show_info:
            return
        t = world.player.get_transform()
        v = world.player.get_velocity()
        c = world.player.get_control()
        compass = world.imu_sensor.compass
        heading = 'N' if compass > 270.5 or compass < 89.5 else ''
        heading += 'S' if 90.5 < compass < 269.5 else ''
        heading += 'E' if 0.5 < compass < 179.5 else ''
        heading += 'W' if 180.5 < compass < 359.5 else ''
        colhist = world.collision_sensor.get_collision_history()
        collision = [colhist[x + self.frame - 200] for x in range(0, 200)]
        max_col = max(1.0, max(collision))
        collision = [x / max_col for x in collision]
        vehicles = world.world.get_actors().filter('vehicle.*')
        # TAG
        # vehicles = [bp for bp in vehicles if not fnmatch.fnmatch(bp.id, 'vehicle.tesla.*')]
        vehicles = [bp for bp in vehicles if not fnmatch.fnmatch(str(bp.id), 'vehicle.tesla.*')]
        # self._info_text = [
        #     'Server:  % 16.0f FPS' % self.server_fps,
        #     'Client:  % 16.0f FPS' % clock.get_fps(),
        #     '',
        #     'Vehicle: % 20s' % get_actor_display_name(world.player, truncate=20),
        #     'Map:     % 20s' % world.map.name.split('/')[-1],
        #     'Simulation time: % 12s' % datetime.timedelta(seconds=int(self.simulation_time)),
        #     '',
        #     'Speed:   % 15.0f km/h' % (3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2)),
        #     u'Compass:% 17.0f\N{DEGREE SIGN} % 2s' % (compass, heading),
        #     'Accelero: (%5.1f,%5.1f,%5.1f)' % (world.imu_sensor.accelerometer),
        #     'Gyroscop: (%5.1f,%5.1f,%5.1f)' % (world.imu_sensor.gyroscope),
        #     'Location:% 20s' % ('(% 5.1f, % 5.1f)' % (t.location.x, t.location.y)),
        #     'GNSS:% 24s' % ('(% 2.6f, % 3.6f)' % (world.gnss_sensor.lat, world.gnss_sensor.lon)),
        #     'Height:  % 18.0f m' % t.location.z,
        #     '']
        self._info_text = [
            'Server:  % 16.0f FPS' % self.server_fps,
            'Client:  % 16.0f FPS' % clock.get_fps(),
            '',
            # 'Map:     % 20s' % world.map.name.split('/')[-1],
            # '',
            '速度:   % 15.0f km/h' % (3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2)),
            u'朝向:% 16.0f\N{DEGREE SIGN} % 2s' % (compass, heading),
            '位置:% 20s' % ('(% 5.1f, % 5.1f)' % (t.location.x, t.location.y)),
            # 'GNSS:% 24s' % ('(% 2.6f, % 3.6f)' % (world.gnss_sensor.lat, world.gnss_sensor.lon)),
            # 'Height:  % 18.0f m' % transform.location.z,
            '']
        # if isinstance(c, carla.VehicleControl):
        #     self._info_text += [
        #         ('Throttle:', c.throttle, 0.0, 1.0),
        #         ('Steer:', c.steer, -1.0, 1.0),
        #         ('Brake:', c.brake, 0.0, 1.0),
        #         ('Reverse:', c.reverse),
        #         ('Hand brake:', c.hand_brake),
        #         ('Manual:', c.manual_gear_shift),
        #         'Gear:        %s' % {-1: 'R', 0: 'N'}.get(c.gear, c.gear)]
        if isinstance(c, carla.VehicleControl):
            self._info_text += [('油门:', c.throttle, 0.0, 1.0),
                                ('轮胎方向:', c.steer, -1.0, 1.0),
                                ('刹车:', c.brake, 0.0, 1.0),
                                ('倒车:', c.reverse),
                                ('手刹:', c.hand_brake),
                                # ('Manual:', control.manual_gear_shift),
                                # 'Gear:        %s' % {
                                #     -1: 'R',
                                #     0: 'N'}.get(control.gear, control.gear)
                                ]

        # if self._show_ackermann_info:
        #         self._info_text += [
        #             '',
        #             'Ackermann Controller:',
        #             '  Target speed: % 8.0f km/h' % (3.6*self._ackermann_control.speed),
        #         ]
        # elif isinstance(c, carla.WalkerControl):
        #     self._info_text += [
        #         ('Speed:', c.speed, 0.0, 5.556),
        #         ('Jump:', c.jump)]
        # self._info_text += [
        #     '',
        #     'Collision:',
        #     collision,
        #     '',
        #     'Number of vehicles: % 8d' % len(vehicles)]
        if len(vehicles) > 1:
            # self._info_text += ['Nearby vehicles:']
            def distance(l): return math.sqrt((l.x - t.location.x)**2 +
                                              (l.y - t.location.y)**2 + (l.z - t.location.z)**2)
            vehicles = [(distance(x.get_location()), x) for x in vehicles if x.id != world.player.id]
            for d, vehicle in sorted(vehicles, key=lambda vehicles: vehicles[0]):
                if d > 200.0:
                    break
                vehicle_type = get_actor_display_name(vehicle, truncate=22)
                # self._info_text.append('% 4dm %s' % (d, vehicle_type))

        self._show_ackermann_info = enabled

    def update_ackermann_control(self, ackermann_control):
        self._ackermann_control = ackermann_control

    def toggle_info(self):
        self._show_info = not self._show_info

    def notification(self, text, seconds=2.0):
        self._notifications.set_text(text, seconds=seconds)

    def error(self, text):
        self._notifications.set_text('Error: %s' % text, (255, 0, 0))

    def render(self, display):
        if self._show_info:
            info_surface = pygame.Surface((220, self.dim[1]))
            display.blit(info_surface, (0, 0))
            v_offset = 4
            bar_h_offset = 100
            bar_width = 106
            for item in self._info_text:
                if v_offset + 18 > self.dim[1]:
                    break
                if isinstance(item, list):
                    if len(item) > 1:
                        pygame.draw.lines(display, (255, 136, 0), False, points, 2)
                    v_offset += 18
                elif isinstance(item, tuple):
                    if isinstance(item[1], bool):
                        rect = pygame.Rect((bar_h_offset, v_offset + 8), (6, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect, 0 if item[1] else 1)
                    else:
                        rect_border = pygame.Rect((bar_h_offset, v_offset + 8), (bar_width, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect_border, 1)
                        f = (item[1] - item[2]) / (item[3] - item[2])
                        if item[2] < 0.0:
                            rect = pygame.Rect((bar_h_offset + f * (bar_width - 6), v_offset + 8), (6, 6))
                        else:
                            rect = pygame.Rect((bar_h_offset, v_offset + 8), (f * bar_width, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect)
                    item = item[0]
                if item:  # At this point has to be a str.
                    surface = self._font_mono.render(item, True, (255, 255, 255))
                    display.blit(surface, (8, v_offset))
                v_offset += 18
        self._notifications.render(display)
        self.help.render(display)


# ==============================================================================
# -- FadingText ----------------------------------------------------------------
# ==============================================================================


class FadingText(object):
    def __init__(self, font, dim, pos):
        self.font = font
        self.dim = dim
        self.pos = pos
        self.seconds_left = 0
        self.surface = pygame.Surface(self.dim)

    def set_text(self, text, color=(255, 255, 255), seconds=2.0):
        text_texture = self.font.render(text, True, color)
        self.surface = pygame.Surface(self.dim)
        self.seconds_left = seconds
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(text_texture, (10, 11))

        self.titleRightInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        delta_seconds = 1e-3 * clock.get_time()
        self.seconds_left = max(0.0, self.seconds_left - delta_seconds)

    def render(self, display):
        display.blit(self.surface, self.pos)


# ==============================================================================
# -- HelpText ------------------------------------------------------------------
# ==============================================================================


class HelpText(object):
    """Helper class to handle text output using pygame"""

    def __init__(self, font, width, height):
        lines = __doc__.split('\n')
        self.font = font
        self.line_space = 18
        self.dim = (780, len(lines) * self.line_space + 12)
        self.pos = (0.5 * width - 0.5 * self.dim[0], 0.5 * height - 0.5 * self.dim[1])
        self.seconds_left = 0
        self.surface = pygame.Surface(self.dim)
        self.surface.fill((0, 0, 0, 0))
        for n, line in enumerate(lines):
            text_texture = self.font.render(line, True, (255, 255, 255))
            self.surface.blit(text_texture, (22, n * self.line_space))
            self._render = False
        self.surface.set_alpha(220)

    def toggle(self):
        self._render = not self._render

    def render(self, display):
        if self._render:
            display.blit(self.surface, self.pos)


# ==============================================================================
# -- CollisionSensor -----------------------------------------------------------
# ==============================================================================


class CollisionSensor(object):
    def __init__(self, parent_actor, hud):
        self.sensor = None
        self.history = []
        self._parent = parent_actor
        self.hud = hud
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.collision')
        self.sensor = world.spawn_actor(bp, carla.Transform(), attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: CollisionSensor._on_collision(weak_self, event))

    def get_collision_history(self):
        history = collections.defaultdict(int)
        for frame, intensity in self.history:
            history[frame] += intensity
        return history

    @staticmethod
    def _on_collision(weak_self, event):
        self = weak_self()
        if not self:
        actor_type = get_actor_display_name(event.other_actor)
        impulse = event.normal_impulse
        intensity = math.sqrt(impulse.x**2 + impulse.y**2 + impulse.z**2)
        self.history.append((event.frame, intensity))
        if len(self.history) > 4000:
            self.history.pop(0)


# ==============================================================================
# -- LaneInvasionSensor --------------------------------------------------------
# ==============================================================================


class LaneInvasionSensor(object):
    def __init__(self, parent_actor, hud):
        self.sensor = None

        # If the spawn object is not a vehicle, we cannot use the Lane Invasion Sensor
        if parent_actor.type_id.startswith("vehicle."):
            self._parent = parent_actor
            self.hud = hud
            world = self._parent.get_world()
            bp = world.get_blueprint_library().find('sensor.other.lane_invasion')
            self.sensor = world.spawn_actor(bp, carla.Transform(), attach_to=self._parent)
            # We need to pass the lambda a weak reference to self to avoid circular
            # reference.
            weak_self = weakref.ref(self)
            self.sensor.listen(lambda event: LaneInvasionSensor._on_invasion(weak_self, event))

    @staticmethod
    def _on_invasion(weak_self, event):
        self = weak_self()
        if not self:
            return
        lane_types = set(x.type for x in event.crossed_lane_markings)
        text = ['%r' % str(x).split()[-1] for x in lane_types]
        self.hud.notification('Crossed line %s' % ' and '.join(text))


# ==============================================================================
# -- GnssSensor ----------------------------------------------------------------
        __qtablewidgetitem.setBackground(QColor(0, 0, 0))


class GnssSensor(object):
    def __init__(self, parent_actor):
        self.sensor = None
        self._parent = parent_actor
        self.lat = 0.0
        self.lon = 0.0
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.gnss')
        self.sensor = world.spawn_actor(bp, carla.Transform(carla.Location(x=1.0, z=2.8)), attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: GnssSensor._on_gnss_event(weak_self, event))

    @staticmethod
    def _on_gnss_event(weak_self, event):
        self = weak_self()
        if not self:
            return
        self.lat = event.latitude
        self.lon = event.longitude


# ==============================================================================
# -- IMUSensor -----------------------------------------------------------------
# ==============================================================================


class IMUSensor(object):
    def __init__(self, parent_actor):
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter)
        self._parent = parent_actor
        self.accelerometer = (0.0, 0.0, 0.0)
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter)
        self.compass = 0.0
        world = self._parent.get_world()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter)
        self.sensor = world.spawn_actor(
            bp, carla.Transform(), attach_to=self._parent)
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter)
        # reference.
        weak_self = weakref.ref(self)
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter)
            lambda sensor_data: IMUSensor._IMU_callback(weak_self, sensor_data))

        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter)
    def _IMU_callback(weak_self, sensor_data):
        self = weak_self()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter)
            return
        limits = (-99.9, 99.9)
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter)
            max(limits[0], min(limits[1], sensor_data.accelerometer.x)),
            max(limits[0], min(limits[1], sensor_data.accelerometer.y)),
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter)
        self.gyroscope = (
            max(limits[0], min(limits[1], math.degrees(sensor_data.gyroscope.x))),
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter)
            max(limits[0], min(limits[1], math.degrees(sensor_data.gyroscope.z))))
        self.compass = math.degrees(sensor_data.compass)
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter)

# ==============================================================================
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter)
# ==============================================================================

        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter)
class RadarSensor(object):
    def __init__(self, parent_actor):
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter)
        self._parent = parent_actor
        bound_x = 0.5 + self._parent.bounding_box.extent.x
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter)
        bound_z = 0.5 + self._parent.bounding_box.extent.z

        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter)
        world = self._parent.get_world()
        self.debug = world.debug
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter)
        bp.set_attribute('horizontal_fov', str(35))
        bp.set_attribute('vertical_fov', str(20))
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter)
            bp,
            carla.Transform(
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter)
                carla.Rotation(pitch=5)),
            attach_to=self._parent)
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter)
        weak_self = weakref.ref(self)
        self.sensor.listen(
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter)

    @staticmethod
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter)
        self = weak_self()
        if not self:
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter)
        # To get a numpy [[vel, altitude, azimuth, depth],...[,,,]]:
        # points = np.frombuffer(radar_data.raw_data, dtype=np.dtype('f4'))
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter)

        current_rot = radar_data.transform.rotation
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter)
            azi = math.degrees(detect.azimuth)
            alt = math.degrees(detect.altitude)
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter)
            # be properly seen
            fw_vec = carla.Vector3D(x=detect.depth - 0.25)
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter)
                carla.Location(),
                carla.Rotation(
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter)
                    yaw=current_rot.yaw + azi,
                    roll=current_rot.roll)).transform(fw_vec)
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter)
            def clamp(min_v, max_v, value):
                return max(min_v, min(value, max_v))
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter)
            norm_velocity = detect.velocity / self.velocity_range  # range [-1, 1]
            r = int(clamp(0.0, 1.0, 1.0 - norm_velocity) * 255.0)
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter)
            b = int(abs(clamp(- 1.0, 0.0, - 1.0 - norm_velocity)) * 255.0)
            self.debug.draw_point(
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter)
                size=0.075,
                life_time=0.06,
                persistent_lines=False,
                color=carla.Color(r, g, b))

# ==============================================================================
# -- CameraManager -------------------------------------------------------------
# ==============================================================================


class CameraManager(object):
    def __init__(self, parent_actor, hud, gamma_correction):
        self.sensor = None
        self.surface = None
        self._parent = parent_actor
        self.hud = hud
        self.recording = False
        bound_x = 0.5 + self._parent.bounding_box.extent.x
        bound_y = 0.5 + self._parent.bounding_box.extent.y
        bound_z = 0.5 + self._parent.bounding_box.extent.z
        Attachment = carla.AttachmentType

        if not self._parent.type_id.startswith("walker.pedestrian"):
            self._camera_transforms = [
                (carla.Transform(carla.Location(x=+0.8*bound_x, y=+0.0*bound_y, z=1.3*bound_z)), Attachment.Rigid),
                (carla.Transform(carla.Location(x=-2.0*bound_x, y=+0.0*bound_y, z=2.0*bound_z),
                                 carla.Rotation(pitch=8.0)), Attachment.SpringArmGhost),
                (carla.Transform(carla.Location(x=+1.9*bound_x, y=+1.0*bound_y, z=1.2*bound_z)), Attachment.SpringArmGhost),
                (carla.Transform(carla.Location(x=-2.8*bound_x, y=+0.0*bound_y, z=4.6*bound_z),
                                 carla.Rotation(pitch=6.0)), Attachment.SpringArmGhost),
                (carla.Transform(carla.Location(x=-1.0, y=-1.0*bound_y, z=0.4*bound_z)), Attachment.Rigid)]
        else:
            self._camera_transforms = [
                (carla.Transform(carla.Location(x=+0.8*bound_x, y=+0.0*bound_y, z=1.3*bound_z)), Attachment.Rigid),
                (carla.Transform(carla.Location(x=-2.0*bound_x, y=+0.0*bound_y, z=2.0*bound_z),
                                 carla.Rotation(pitch=8.0)), Attachment.SpringArmGhost),
                (carla.Transform(carla.Location(x=+1.9*bound_x, y=+1.0*bound_y, z=1.2*bound_z)), Attachment.SpringArmGhost),
                (carla.Transform(carla.Location(x=-2.8*bound_x, y=+0.0*bound_y, z=4.6*bound_z),
                                 carla.Rotation(pitch=6.0)), Attachment.SpringArmGhost),
                (carla.Transform(carla.Location(x=-1.0, y=-1.0*bound_y, z=0.4*bound_z)), Attachment.Rigid)]

        self.transform_index = 1
        self.sensors = [
            ['sensor.camera.rgb', cc.Raw, 'Camera RGB', {}],
            ['sensor.camera.depth', cc.Raw, 'Camera Depth (Raw)', {}],
            # ['sensor.camera.depth', cc.Depth, 'Camera Depth (Gray Scale)', {}],
            # ['sensor.camera.depth', cc.LogarithmicDepth, 'Camera Depth (Logarithmic Gray Scale)', {}],
            ['sensor.camera.semantic_segmentation', cc.Raw, 'Camera Semantic Segmentation (Raw)', {}],
            ['sensor.camera.semantic_segmentation', cc.CityScapesPalette,
                'Camera Semantic Segmentation (CityScapes Palette)', {}],
            # ['sensor.camera.instance_segmentation', cc.CityScapesPalette,
            #     'Camera Instance Segmentation (CityScapes Palette)', {}],
            ['sensor.camera.instance_segmentation', cc.Raw, 'Camera Instance Segmentation (Raw)', {}],
            ['sensor.camera.fisheye', cc.Raw, 'Camera Fisheye', {}],
            ['sensor.camera.dvs', cc.Raw, 'Dynamic Vision Sensor', {}],
            # ['sensor.camera.rgb', cc.Raw, 'Camera RGB Distorted',
            #     {'lens_circle_multiplier': '3.0',
            #      'lens_circle_falloff': '3.0',
            #      'chromatic_aberration_intensity': '0.5',
            #      'chromatic_aberration_offset': '0',
            #      }],
            ['sensor.camera.optical_flow', cc.Raw, 'Optical Flow', {}],
            # ['sensor.camera.normals', cc.Raw, 'Camera Normals', {}],
            ['sensor.lidar.ray_cast', None, 'Lidar (Ray-Cast)', {'range': '50'}],
        ]
        # ]
        world = self._parent.get_world()
        bp_library = world.get_blueprint_library()
        for item in self.sensors:
            bp = bp_library.find(item[0])
            # bp = item[0]
            # if item[0].startswith('sensor.camera'):
            if item[0] == 'sensor.camera.fisheye':
                # bp.set_attribute('x_size', str(hud.dim[0]))
                # bp.set_attribute('y_size', str(hud.dim[1]))
                # bp.set_attribute('max_angle', str(210))
                # bp.set_attribute('d_1', str(0.08309221636708493))
                # bp.set_attribute('d_2', str(0.01112126630599195))
                # bp.set_attribute('d_3', str(-0.008587261043925865))
                # bp.set_attribute('d_4', str(0.0008542188930970716))
                # bp.set_attribute('f_x', str(320))
                # bp.set_attribute('f_y', str(320))
                # bp.set_attribute('c_x', str(640))
                # bp.set_attribute('c_y', str(480))
                bp.set_attribute('x_size', str(hud.dim[0]))
                bp.set_attribute('y_size', str(hud.dim[1]))
                bp.set_attribute('max_angle', str(210))
                bp.set_attribute('d_1', str(0.08309221636708493))
                bp.set_attribute('d_2', str(0.01112126630599195))
                bp.set_attribute('d_3', str(-0.008587261043925865))
                bp.set_attribute('d_4', str(0.0008542188930970716))
                bp.set_attribute('f_x', str(140))
                bp.set_attribute('f_y', str(140))
                bp.set_attribute('c_x', str(350))
                bp.set_attribute('c_y', str(300))
            elif item[0].startswith('sensor.camera'):
                # elif item[0] == 'sensor.camera':
                # bp.set_attribute('image_size_x', str(hud.dim[0]))
                # bp.set_attribute('image_size_y', str(hud.dim[1]))
                # if bp.has_attribute('gamma'):
                #     bp.set_attribute('gamma', str(gamma_correction))
                # for attr_name, attr_value in item[3].items():
                #     bp.set_attribute(attr_name, attr_value)
                bp.set_attribute('image_size_x', str(800))
                bp.set_attribute('image_size_y', str(600))
                if bp.has_attribute('gamma'):
                    bp.set_attribute('gamma', str(gamma_correction))
                # for attr_name, attr_value in item[3].items():
                #     bp.set_attribute(attr_name, attr_value)
                                "background-position: center;\n"
                                "background-repeat: no-repeat;")
                self.lidar_range = 50

                for attr_name, attr_value in item[3].items():
                    bp.set_attribute(attr_name, attr_value)
                    if attr_name == 'range':
                        self.lidar_range = float(attr_value)

            item.append(bp)
        self.index = None

    def toggle_camera(self):
        self.transform_index = (self.transform_index + 1) % len(self._camera_transforms)
        self.set_sensor(self.index, notify=False, force_respawn=True)

    def set_sensor(self, index, notify=True, force_respawn=False):
        index = index % len(self.sensors)
        needs_respawn = True if self.index is None else \
            (force_respawn or (self.sensors[index][2] != self.sensors[self.index][2]))
        if needs_respawn:
            if self.sensor is not None:
                self.sensor.destroy()
                self.surface = None
            self.sensor = self._parent.get_world().spawn_actor(
                self.sensors[index][-1],
                self._camera_transforms[self.transform_index][0],
                attach_to=self._parent,
                attachment_type=self._camera_transforms[self.transform_index][1])
            # We need to pass the lambda a weak reference to self to avoid
            # circular reference.
            weak_self = weakref.ref(self)
            self.sensor.listen(lambda image: CameraManager._parse_image(weak_self, image))
        if notify:
            self.hud.notification(self.sensors[index][2])
        self.index = index

    def next_sensor(self):
        self.set_sensor(self.index + 1)

    def toggle_recording(self):
        self.recording = not self.recording
        self.hud.notification('Recording %s' % ('On' if self.recording else 'Off'))

    def render(self, display):
        if self.surface is not None:
            display.blit(self.surface, (0, 0))

        self.labelBoxBlenderInstalation.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
    def _parse_image(weak_self, image):
        self = weak_self()
            return
        if self.sensors[self.index][0].startswith('sensor.lidar'):
            # if self.sensors[self.index][0] == 'sensor.lidar':
            points = np.frombuffer(image.raw_data, dtype=np.dtype('f4'))
            points = np.reshape(points, (int(points.shape[0] / 4), 4))
            lidar_data = np.array(points[:, :2])
            lidar_data *= min(self.hud.dim) / (2.0 * self.lidar_range)
            lidar_data += (0.5 * self.hud.dim[0], 0.5 * self.hud.dim[1])
            lidar_data = np.fabs(lidar_data)  # pylint: disable=E1111
            lidar_data = lidar_data.astype(np.int32)
            lidar_data = np.reshape(lidar_data, (-1, 2))
            lidar_img_size = (self.hud.dim[0], self.hud.dim[1], 3)
            lidar_img = np.zeros((lidar_img_size), dtype=np.uint8)
            lidar_img[tuple(lidar_data.T)] = (255, 255, 255)
            self.surface = pygame.surfarray.make_surface(lidar_img)
        # elif self.sensors[self.index][0] == 'sensor.camera.dvs':
        elif self.sensors[self.index][0].startswith('sensor.camera.dvs'):
            # Example of converting the raw_data from a carla.DVSEventArray
            # sensor into a NumPy array and using it as an image
            dvs_events = np.frombuffer(image.raw_data, dtype=np.dtype([
                ('x', np.uint16), ('y', np.uint16), ('t', np.int64), ('pol', np.bool)]))
            dvs_img = np.zeros((image.height, image.width, 3), dtype=np.uint8)
            # Blue is positive, red is negative
            dvs_img[dvs_events[:]['y'], dvs_events[:]['x'], dvs_events[:]['pol'] * 2] = 255
            self.surface = pygame.surfarray.make_surface(dvs_img.swapaxes(0, 1))
        # elif self.sensors[self.index][0] == 'sensor.camera.optical_flow':
        elif self.sensors[self.index][0].startswith('sensor.camera.optical_flow'):
            image = image.get_color_coded_flow()
            array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
            array = np.reshape(array, (image.height, image.width, 4))
            array = array[:, :, :3]
            self.surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
        else:
            array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
            array = array[:, :, :3]
            array = array[:, :, ::-1]
            self.surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
        if self.recording:
            image.save_to_disk('_out/%08d' % image.frame)


# ==============================================================================
# -- game_loop() ---------------------------------------------------------------
# ==============================================================================


def game_loop(args):
    pygame.init()
    pygame.font.init()
    world = None
    original_settings = None

    try:
        client = carla.Client(args.host, args.port)
        client.set_timeout(2000.0)

        sim_world = client.get_world()
        if args.sync:
            original_settings = sim_world.get_settings()
            settings = sim_world.get_settings()
                settings.synchronous_mode = True
            sim_world.apply_settings(settings)

            traffic_manager = client.get_trafficmanager()
            traffic_manager.set_synchronous_mode(True)

        if args.autopilot and not sim_world.get_settings().synchronous_mode:
            print("WARNING: You are currently in asynchronous mode and could "
                  "experience some issues with the traffic simulation")

        display = pygame.display.set_mode(
            (args.width, args.height),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        display.fill((0, 0, 0))
        pygame.display.flip()

        hud = HUD(args.width, args.height)
        world = World(sim_world, hud, args)
        controller = KeyboardControl(world, args.autopilot)

        if args.sync:
            sim_world.tick()
        else:
            sim_world.wait_for_tick()

        clock = pygame.time.Clock()
        while True:
            if args.sync:
                sim_world.tick()
            clock.tick_busy_loop(60)
            if controller.parse_events(client, world, clock, args.sync):
                return
            world.tick(clock)
            world.render(display)
            pygame.display.flip()

    finally:

        if original_settings:
            sim_world.apply_settings(original_settings)
        __qtablewidgetitem49.setBackground(QColor(0, 0, 0))
        if (world and world.recording_enabled):
            client.stop_recorder()

        if world is not None:
            world.destroy()

        __qtablewidgetitem51.setFont(font)


# ==============================================================================
# -- main() --------------------------------------------------------------------
# ==============================================================================


def main():
    argparser = argparse.ArgumentParser(
        description='CARLA Manual Control Client')
    argparser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='debug',
        help='print debug information')
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '-a', '--autopilot',
        action='store_true',
        help='enable autopilot')
    argparser.add_argument(
        '--res',
        metavar='WIDTHxHEIGHT',
        default='800x600',
        help='window resolution (default: 1280x720)')
    argparser.add_argument(
        '--filter',
        metavar='PATTERN',
        default='vehicle.tesla.model3',
        help='actor filter (default: "vehicle.tesla.model3")')
    argparser.add_argument(
        '--generation',
        metavar='G',
        default='2',
        help='restrict to certain actor generation (values: "1","2","All" - default: "2")')
    argparser.add_argument(
        '--rolename',
        metavar='NAME',
        default='hero',
        help='actor role name (default: "hero")')
    argparser.add_argument(
        '--gamma',
        default=2.2,
        type=float,
        help='Gamma correction of the camera (default: 2.2)')
    argparser.add_argument(
        '--sync',
        action='store_true',
        help='Activate synchronous mode execution')
    args = argparser.parse_args()

    args.width, args.height = [int(x) for x in args.res.split('x')]

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)

    logging.info('listening to server %s:%s', args.host, args.port)

    # print(__doc__)

    try:

        game_loop(args)

    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')


if __name__ == '__main__':

    main()
        self.creditsLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "hr { height: 1px; border-width: 0; }\n"
                                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                                         "</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">VisionVoyage</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u4e00\u6b3e\u57fa\u4e8e\u9c7c\u773c\u76f8\u673a\u4e0e\u5176\u4ed6\u611f\u77e5\u6280\u672f\u7684\u81ea\u52a8\u9a7e\u9a76"
                                                         "\u4eff\u771f\u7cfb\u7edf\u3002</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">MIT License</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Ingenuity Drive</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u4e2a\u6027\u5316\u5b9a\u5236</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">\u60a8\u53ef\u4ee5\u901a\u8fc7\u4e0b\u65b9\u201c\u8054\u7cfb\u6211\u4eec\u201d\u6765\u5411\u6211"
                                                         "\u53f8\u5546\u8ba8\u4e2a\u6027\u5316\u5b9a\u5236\u65b9\u6848\uff0c\u6211\u53f8\u4f1a\u5b9a\u5236\u60a8\u6240\u9700\u7684\u4eff\u771f\u5730\u56fe\u548c\u8f66\u8f86\u6a21\u578b\u4ee5\u53ca\u63d0\u4f9b\u4e13\u4e1a\u7684\u6280\u672f\u652f\u6301\uff0c\u4f7f\u60a8\u83b7\u5f97\u72ec\u7279\u7684\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f\u4f53\u9a8c\u3002</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u8054\u7cfb\u6211\u4eec</span></p>\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">M0rtzz E-mail : m0rtzz@163.com</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">VisionVoyage Client</span></p></body></html>", None))
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e", None))
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u7528", None))
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e", None))
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u7528", None))
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"W/S", None))
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u524d\u8fdb/\u5239\u8f66", None))
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"TAB", None))
        ___qtablewidgetitem18.setText(QCoreApplication.translate(
            "MainWindow", u"\u6539\u53d8\u4f20\u611f\u5668\u4f4d\u7f6e", None))
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"A/D", None))
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u5de6/\u53f3\u8f6c\u5411", None))
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"N", None))
        ___qtablewidgetitem22.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e0b\u4e00\u4e2a\u4f20\u611f\u5668", None))
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u624b\u5239", None))
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362HUD\u663e\u793a", None))
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"TAB", None))
        ___qtablewidgetitem28.setText(QCoreApplication.translate(
            "MainWindow", u"\u6539\u53d8\u4f20\u611f\u5668\u4f4d\u7f6e", None))
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"R", None))
        ___qtablewidgetitem30.setText(QCoreApplication.translate(
            "MainWindow", u"\u8bb0\u5f55\u56fe\u50cf\u5230\u78c1\u76d8", None))
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"N", None))
        ___qtablewidgetitem32.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e0b\u4e00\u4e2a\u4f20\u611f\u5668", None))
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"ESC", None))
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"[1-9]", None))
        ___qtablewidgetitem36.setText(QCoreApplication.translate(
            "MainWindow", u"\u5207\u6362\u81f3\u4f20\u611f\u5668[1-9]", None))
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362HUD\u663e\u793a", None))
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"R", None))
        ___qtablewidgetitem40.setText(QCoreApplication.translate(
            "MainWindow", u"\u8bb0\u5f55\u56fe\u50cf\u5230\u78c1\u76d8", None))
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"C", None))
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u5929\u6c14", None))
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"V", None))
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u5c42", None))
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"B/SHIFT+B", None))
        ___qtablewidgetitem46.setText(QCoreApplication.translate(
            "MainWindow", u"\u52a0\u8f7d/\u5378\u8f7d\u56fe\u5c42", None))
        self.lineEdit.setText(QCoreApplication.translate(
            "MainWindow", u"\u5feb\u6377\u952e\u64cd\u4f5c\u8bf4\u660e", None))
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u865a\u62df\u9a7e\u9a76", None))
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u9a7e\u9a76", None))
        self.btn_fisheye_one2one.setText(QCoreApplication.translate(
            "MainWindow", u"\u666e\u901a\u56fe\u50cf\u8f6c\u9c7c\u773c\u56fe\u50cf", None))
        self.btn_fisheye_five2one.setText(QCoreApplication.translate(
            "MainWindow", u"\u591a\u5f20\u666e\u901a\u56fe\u50cf\u62fc\u63a5\u9c7c\u773c\u56fe\u50cf", None))
        self.btn_segmentation_image.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e0a\u4f20\u56fe\u50cf\u8fdb\u884c\u5206\u5272", None))
        self.btn_segmentation_video.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e0a\u4f20\u89c6\u9891\u8fdb\u884c\u5b9e\u65f6\u5206\u5272", None))
        self.btn_get_fisheye.setText(QCoreApplication.translate(
            "MainWindow", u"\u83b7\u53d6\u9c7c\u773c\u56fe\u50cf", None))
        self.btn_get_common.setText(QCoreApplication.translate(
            "MainWindow", u"\u83b7\u53d6\u5176\u4ed6\u975e\u7578\u53d8\u4f20\u611f\u5668\u56fe\u50cf", None))
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u9c7c\u773c\u56fe\u50cf", None))
        ___qtablewidgetitem50.setText(QCoreApplication.translate(
            "MainWindow", u"\u5176\u4ed6\u975e\u7578\u53d8\u4f20\u611f\u5668\u56fe\u50cf", None))
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None))
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None))
