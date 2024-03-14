# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 686)
        MainWindow.setMinimumSize(QSize(940, 560))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font1)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloud-upload.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_image = QPushButton(self.topMenu)
        self.btn_image.setObjectName(u"btn_image")
        sizePolicy.setHeightForWidth(self.btn_image.sizePolicy().hasHeightForWidth())
        self.btn_image.setSizePolicy(sizePolicy)
        self.btn_image.setMinimumSize(QSize(0, 45))
        self.btn_image.setFont(font1)
        self.btn_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_image.setLayoutDirection(Qt.LeftToRight)
        self.btn_image.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image-plus.png);")

        self.verticalLayout_8.addWidget(self.btn_image)

        self.btn_simulation = QPushButton(self.topMenu)
        self.btn_simulation.setObjectName(u"btn_simulation")
        sizePolicy.setHeightForWidth(self.btn_simulation.sizePolicy().hasHeightForWidth())
        self.btn_simulation.setSizePolicy(sizePolicy)
        self.btn_simulation.setMinimumSize(QSize(0, 45))
        self.btn_simulation.setFont(font1)
        self.btn_simulation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_simulation.setLayoutDirection(Qt.LeftToRight)
        self.btn_simulation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_simulation)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_personal_center = QPushButton(self.bottomMenu)
        self.btn_personal_center.setObjectName(u"btn_personal_center")
        sizePolicy.setHeightForWidth(self.btn_personal_center.sizePolicy().hasHeightForWidth())
        self.btn_personal_center.setSizePolicy(sizePolicy)
        self.btn_personal_center.setMinimumSize(QSize(0, 45))
        self.btn_personal_center.setFont(font1)
        self.btn_personal_center.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_personal_center.setLayoutDirection(Qt.LeftToRight)
        self.btn_personal_center.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")

        self.verticalLayout_9.addWidget(self.btn_personal_center)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_start_server = QPushButton(self.extraTopMenu)
        self.btn_start_server.setObjectName(u"btn_start_server")
        sizePolicy.setHeightForWidth(self.btn_start_server.sizePolicy().hasHeightForWidth())
        self.btn_start_server.setSizePolicy(sizePolicy)
        self.btn_start_server.setMinimumSize(QSize(0, 45))
        self.btn_start_server.setFont(font1)
        self.btn_start_server.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_server.setLayoutDirection(Qt.LeftToRight)
        self.btn_start_server.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-link.png);")

        self.verticalLayout_11.addWidget(self.btn_start_server)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font1)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_my_image = QPushButton(self.extraTopMenu)
        self.btn_my_image.setObjectName(u"btn_my_image")
        sizePolicy.setHeightForWidth(self.btn_my_image.sizePolicy().hasHeightForWidth())
        self.btn_my_image.setSizePolicy(sizePolicy)
        self.btn_my_image.setMinimumSize(QSize(0, 45))
        self.btn_my_image.setFont(font1)
        self.btn_my_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_my_image.setLayoutDirection(Qt.LeftToRight)
        self.btn_my_image.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image1.png);")

        self.verticalLayout_11.addWidget(self.btn_my_image)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.widget_4 = QWidget(self.pagesContainer)
        self.widget_4.setObjectName(u"widget_4")
        self.stackedWidget = QStackedWidget(self.widget_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 845, 559))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.simulation_page = QWidget()
        self.simulation_page.setObjectName(u"simulation_page")
        self.table_widget_operation_help = QTableWidget(self.simulation_page)
        if (self.table_widget_operation_help.columnCount() < 4):
            self.table_widget_operation_help.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        self.table_widget_operation_help.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_operation_help.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_operation_help.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget_operation_help.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_widget_operation_help.rowCount() < 11):
            self.table_widget_operation_help.setRowCount(11)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_widget_operation_help.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(0, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(0, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(1, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(1, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(1, 2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(1, 3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(2, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(2, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(2, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(3, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(3, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(3, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(3, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(4, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(4, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(4, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(4, 3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(5, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(5, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(6, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(6, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(7, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(7, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(8, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(8, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(9, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(9, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(10, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.table_widget_operation_help.setItem(10, 1, __qtablewidgetitem46)
        self.table_widget_operation_help.setObjectName(u"table_widget_operation_help")
        self.table_widget_operation_help.setGeometry(QRect(0, 70, 821, 411))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_widget_operation_help.sizePolicy().hasHeightForWidth())
        self.table_widget_operation_help.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_widget_operation_help.setPalette(palette)
        self.table_widget_operation_help.setFont(font1)
        self.table_widget_operation_help.setFrameShape(QFrame.NoFrame)
        self.table_widget_operation_help.setLineWidth(1)
        self.table_widget_operation_help.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget_operation_help.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget_operation_help.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_widget_operation_help.setAutoScroll(True)
        self.table_widget_operation_help.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget_operation_help.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget_operation_help.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget_operation_help.setShowGrid(True)
        self.table_widget_operation_help.setGridStyle(Qt.SolidLine)
        self.table_widget_operation_help.setSortingEnabled(False)
        self.table_widget_operation_help.setRowCount(11)
        self.table_widget_operation_help.horizontalHeader().setVisible(True)
        self.table_widget_operation_help.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget_operation_help.horizontalHeader().setMinimumSectionSize(100)
        self.table_widget_operation_help.horizontalHeader().setDefaultSectionSize(200)
        self.table_widget_operation_help.horizontalHeader().setHighlightSections(True)
        self.table_widget_operation_help.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_widget_operation_help.horizontalHeader().setStretchLastSection(False)
        self.table_widget_operation_help.verticalHeader().setVisible(False)
        self.table_widget_operation_help.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget_operation_help.verticalHeader().setMinimumSectionSize(33)
        self.table_widget_operation_help.verticalHeader().setDefaultSectionSize(33)
        self.table_widget_operation_help.verticalHeader().setHighlightSections(False)
        self.table_widget_operation_help.verticalHeader().setStretchLastSection(True)
        self.line_edit_operation_help = QLineEdit(self.simulation_page)
        self.line_edit_operation_help.setObjectName(u"line_edit_operation_help")
        self.line_edit_operation_help.setGeometry(QRect(10, 0, 801, 31))
        self.line_edit_operation_help.setAlignment(Qt.AlignCenter)
        self.line_edit_operation_help.setReadOnly(True)
        self.tableWidget = QTableWidget(self.simulation_page)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 30, 821, 51))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(400)
        self.widget_9 = QWidget(self.simulation_page)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(9, 490, 801, 60))
        self.btn_generate_traffic = QPushButton(self.widget_9)
        self.btn_generate_traffic.setObjectName(u"btn_generate_traffic")
        self.btn_generate_traffic.setGeometry(QRect(0, 0, 267, 60))
        self.btn_manual_control = QPushButton(self.widget_9)
        self.btn_manual_control.setObjectName(u"btn_manual_control")
        self.btn_manual_control.setGeometry(QRect(267, 0, 267, 60))
        self.btn_automatic_control = QPushButton(self.widget_9)
        self.btn_automatic_control.setObjectName(u"btn_automatic_control")
        self.btn_automatic_control.setGeometry(QRect(534, 0, 267, 60))
        self.stackedWidget.addWidget(self.simulation_page)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/VisionVoyage_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.row_1 = QFrame(self.row_2)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setLayoutDirection(Qt.LeftToRight)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")
        self.labelBoxBlenderInstalation.setTextFormat(Qt.AutoText)
        self.labelBoxBlenderInstalation.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.btn_open_dir = QPushButton(self.frame_content_wid_1)
        self.btn_open_dir.setObjectName(u"btn_open_dir")
        self.btn_open_dir.setMinimumSize(QSize(150, 30))
        self.btn_open_dir.setFont(font1)
        self.btn_open_dir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_dir.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_dir.setIcon(icon4)

        self.gridLayout.addWidget(self.btn_open_dir, 0, 1, 1, 1)

        self.line_edit_filenames = QLineEdit(self.frame_content_wid_1)
        self.line_edit_filenames.setObjectName(u"line_edit_filenames")
        self.line_edit_filenames.setMinimumSize(QSize(0, 30))
        self.line_edit_filenames.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.line_edit_filenames, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)

        self.widget = QWidget(self.row_1)
        self.widget.setObjectName(u"widget")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, -10, 811, 291))
        self.widget_2.setTabletTracking(False)
        self.table_widget_transform_upload_result = QTableWidget(self.widget_2)
        if (self.table_widget_transform_upload_result.columnCount() < 3):
            self.table_widget_transform_upload_result.setColumnCount(3)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setBackground(QColor(0, 0, 0));
        self.table_widget_transform_upload_result.setHorizontalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setHorizontalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setHorizontalHeaderItem(2, __qtablewidgetitem51)
        if (self.table_widget_transform_upload_result.rowCount() < 23):
            self.table_widget_transform_upload_result.setRowCount(23)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font);
        self.table_widget_transform_upload_result.setVerticalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(6, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(7, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(8, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(9, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(10, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(11, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(12, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(13, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(14, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(15, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(16, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(17, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(18, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(19, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(20, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(21, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setVerticalHeaderItem(22, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setItem(0, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.table_widget_transform_upload_result.setItem(0, 1, __qtablewidgetitem76)
        self.table_widget_transform_upload_result.setObjectName(u"table_widget_transform_upload_result")
        self.table_widget_transform_upload_result.setGeometry(QRect(-10, 0, 821, 301))
        sizePolicy3.setHeightForWidth(self.table_widget_transform_upload_result.sizePolicy().hasHeightForWidth())
        self.table_widget_transform_upload_result.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_widget_transform_upload_result.setPalette(palette1)
        self.table_widget_transform_upload_result.setFont(font1)
        self.table_widget_transform_upload_result.setLayoutDirection(Qt.LeftToRight)
        self.table_widget_transform_upload_result.setFrameShape(QFrame.NoFrame)
        self.table_widget_transform_upload_result.setLineWidth(1)
        self.table_widget_transform_upload_result.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_widget_transform_upload_result.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget_transform_upload_result.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_widget_transform_upload_result.setAutoScroll(True)
        self.table_widget_transform_upload_result.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget_transform_upload_result.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget_transform_upload_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget_transform_upload_result.setShowGrid(True)
        self.table_widget_transform_upload_result.setGridStyle(Qt.SolidLine)
        self.table_widget_transform_upload_result.setSortingEnabled(False)
        self.table_widget_transform_upload_result.setColumnCount(3)
        self.table_widget_transform_upload_result.horizontalHeader().setVisible(True)
        self.table_widget_transform_upload_result.horizontalHeader().setCascadingSectionResizes(True)
        self.table_widget_transform_upload_result.horizontalHeader().setMinimumSectionSize(24)
        self.table_widget_transform_upload_result.horizontalHeader().setDefaultSectionSize(270)
        self.table_widget_transform_upload_result.horizontalHeader().setHighlightSections(False)
        self.table_widget_transform_upload_result.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_widget_transform_upload_result.horizontalHeader().setStretchLastSection(True)
        self.table_widget_transform_upload_result.verticalHeader().setVisible(False)
        self.table_widget_transform_upload_result.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget_transform_upload_result.verticalHeader().setMinimumSectionSize(21)
        self.table_widget_transform_upload_result.verticalHeader().setHighlightSections(False)
        self.table_widget_transform_upload_result.verticalHeader().setProperty("showSortIndicator", False)
        self.table_widget_transform_upload_result.verticalHeader().setStretchLastSection(True)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 300, 801, 101))
        self.btn_segmentation_image = QPushButton(self.widget_3)
        self.btn_segmentation_image.setObjectName(u"btn_segmentation_image")
        self.btn_segmentation_image.setGeometry(QRect(0, 50, 401, 51))
        self.btn_segmentation_video = QPushButton(self.widget_3)
        self.btn_segmentation_video.setObjectName(u"btn_segmentation_video")
        self.btn_segmentation_video.setGeometry(QRect(400, 50, 401, 51))
        self.btn_fisheye_one2one = QPushButton(self.widget_3)
        self.btn_fisheye_one2one.setObjectName(u"btn_fisheye_one2one")
        self.btn_fisheye_one2one.setGeometry(QRect(0, 0, 401, 51))
        self.btn_fisheye_five2one = QPushButton(self.widget_3)
        self.btn_fisheye_five2one.setObjectName(u"btn_fisheye_five2one")
        self.btn_fisheye_five2one.setGeometry(QRect(400, 0, 401, 51))

        self.verticalLayout_16.addWidget(self.widget)


        self.verticalLayout_19.addWidget(self.row_1)


        self.verticalLayout.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.widgets)
        self.image_page = QWidget()
        self.image_page.setObjectName(u"image_page")
        self.verticalLayout_20 = QVBoxLayout(self.image_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_5 = QWidget(self.image_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 0, 830, 221))
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(415, 0, 415, 215))
        self.label.setPixmap(QPixmap(u":/images/images/images/sensors.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 415, 215))
        self.label_3.setPixmap(QPixmap(u":/images/images/images/fisheye_collage.png"))
        self.label_3.setScaledContents(True)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 209, 830, 331))
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 9, 828, 51))
        self.btn_get_fisheye = QPushButton(self.widget_8)
        self.btn_get_fisheye.setObjectName(u"btn_get_fisheye")
        self.btn_get_fisheye.setGeometry(QRect(0, 0, 415, 50))
        self.btn_get_common = QPushButton(self.widget_8)
        self.btn_get_common.setObjectName(u"btn_get_common")
        self.btn_get_common.setGeometry(QRect(415, 0, 411, 50))
        self.table_widget_get_image = QTableWidget(self.widget_7)
        if (self.table_widget_get_image.columnCount() < 2):
            self.table_widget_get_image.setColumnCount(2)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setBackground(QColor(0, 0, 0));
        self.table_widget_get_image.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.table_widget_get_image.setHorizontalHeaderItem(1, __qtablewidgetitem78)
        if (self.table_widget_get_image.rowCount() < 23):
            self.table_widget_get_image.setRowCount(23)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font);
        self.table_widget_get_image.setVerticalHeaderItem(0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(4, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(5, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(6, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(7, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(8, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(9, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(10, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(11, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(12, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(13, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(14, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(15, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(16, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(17, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(18, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(19, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(20, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(21, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.table_widget_get_image.setVerticalHeaderItem(22, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.table_widget_get_image.setItem(0, 0, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.table_widget_get_image.setItem(0, 1, __qtablewidgetitem103)
        self.table_widget_get_image.setObjectName(u"table_widget_get_image")
        self.table_widget_get_image.setGeometry(QRect(-10, 100, 841, 231))
        sizePolicy3.setHeightForWidth(self.table_widget_get_image.sizePolicy().hasHeightForWidth())
        self.table_widget_get_image.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_widget_get_image.setPalette(palette2)
        self.table_widget_get_image.setFont(font1)
        self.table_widget_get_image.setFrameShape(QFrame.NoFrame)
        self.table_widget_get_image.setLineWidth(1)
        self.table_widget_get_image.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_widget_get_image.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget_get_image.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_widget_get_image.setAutoScroll(True)
        self.table_widget_get_image.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget_get_image.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_widget_get_image.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget_get_image.setShowGrid(True)
        self.table_widget_get_image.setGridStyle(Qt.SolidLine)
        self.table_widget_get_image.setSortingEnabled(False)
        self.table_widget_get_image.horizontalHeader().setVisible(True)
        self.table_widget_get_image.horizontalHeader().setCascadingSectionResizes(True)
        self.table_widget_get_image.horizontalHeader().setMinimumSectionSize(24)
        self.table_widget_get_image.horizontalHeader().setDefaultSectionSize(412)
        self.table_widget_get_image.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_widget_get_image.horizontalHeader().setStretchLastSection(True)
        self.table_widget_get_image.verticalHeader().setVisible(False)
        self.table_widget_get_image.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget_get_image.verticalHeader().setMinimumSectionSize(21)
        self.table_widget_get_image.verticalHeader().setHighlightSections(False)
        self.table_widget_get_image.verticalHeader().setStretchLastSection(True)
        self.btn_raw_to_platte = QPushButton(self.widget_7)
        self.btn_raw_to_platte.setObjectName(u"btn_raw_to_platte")
        self.btn_raw_to_platte.setGeometry(QRect(0, 60, 826, 51))

        self.verticalLayout_20.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.image_page)

        self.verticalLayout_15.addWidget(self.widget_4)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_send_mail = QPushButton(self.topMenus)
        self.btn_send_mail.setObjectName(u"btn_send_mail")
        sizePolicy.setHeightForWidth(self.btn_send_mail.sizePolicy().hasHeightForWidth())
        self.btn_send_mail.setSizePolicy(sizePolicy)
        self.btn_send_mail.setMinimumSize(QSize(0, 45))
        self.btn_send_mail.setFont(font1)
        self.btn_send_mail.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_mail.setLayoutDirection(Qt.LeftToRight)
        self.btn_send_mail.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_send_mail)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"VisionVoyage", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Created by: Ingenuity Drive", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u754c\u9762", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.btn_image.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u6570\u636e\u96c6", None))
        self.btn_simulation.setText(QCoreApplication.translate("MainWindow", u"\u9a7e\u9a76\u4eff\u771f", None))
        self.btn_personal_center.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close \u6211\u7684", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_start_server.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8 VisionVoyage \u670d\u52a1\u5668", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3b\u9898", None))
        self.btn_my_image.setText(QCoreApplication.translate("MainWindow", u"\u6211\u7684\u56fe\u50cf", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">M0rtzz E-mail : m0rtzz@outlook.com</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/images/IngenuityDr"
                        "ive.png\" /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; color:#ffffff;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">VisionVoyage Client</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        ___qtablewidgetitem = self.table_widget_operation_help.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e", None));
        ___qtablewidgetitem1 = self.table_widget_operation_help.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u7528", None));
        ___qtablewidgetitem2 = self.table_widget_operation_help.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u952e", None));
        ___qtablewidgetitem3 = self.table_widget_operation_help.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u7528", None));
        ___qtablewidgetitem4 = self.table_widget_operation_help.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.table_widget_operation_help.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.table_widget_operation_help.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.table_widget_operation_help.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.table_widget_operation_help.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.table_widget_operation_help.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.table_widget_operation_help.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.table_widget_operation_help.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.table_widget_operation_help.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.table_widget_operation_help.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.table_widget_operation_help.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.table_widget_operation_help.isSortingEnabled()
        self.table_widget_operation_help.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.table_widget_operation_help.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"W/S", None));
        ___qtablewidgetitem16 = self.table_widget_operation_help.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u524d\u8fdb/\u5239\u8f66", None));
        ___qtablewidgetitem17 = self.table_widget_operation_help.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"TAB", None));
        ___qtablewidgetitem18 = self.table_widget_operation_help.item(0, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u4f20\u611f\u5668\u4f4d\u7f6e", None));
        ___qtablewidgetitem19 = self.table_widget_operation_help.item(1, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"A/D", None));
        ___qtablewidgetitem20 = self.table_widget_operation_help.item(1, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u5de6/\u53f3\u8f6c\u5411", None));
        ___qtablewidgetitem21 = self.table_widget_operation_help.item(1, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem22 = self.table_widget_operation_help.item(1, 3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u4e2a\u4f20\u611f\u5668", None));
        ___qtablewidgetitem23 = self.table_widget_operation_help.item(2, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Space", None));
        ___qtablewidgetitem24 = self.table_widget_operation_help.item(2, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u624b\u5239", None));
        ___qtablewidgetitem25 = self.table_widget_operation_help.item(2, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"F1", None));
        ___qtablewidgetitem26 = self.table_widget_operation_help.item(2, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362HUD\u663e\u793a", None));
        ___qtablewidgetitem27 = self.table_widget_operation_help.item(3, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"TAB", None));
        ___qtablewidgetitem28 = self.table_widget_operation_help.item(3, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u4f20\u611f\u5668\u4f4d\u7f6e", None));
        ___qtablewidgetitem29 = self.table_widget_operation_help.item(3, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"R", None));
        ___qtablewidgetitem30 = self.table_widget_operation_help.item(3, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u56fe\u50cf\u5230\u78c1\u76d8", None));
        ___qtablewidgetitem31 = self.table_widget_operation_help.item(4, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem32 = self.table_widget_operation_help.item(4, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u4e2a\u4f20\u611f\u5668", None));
        ___qtablewidgetitem33 = self.table_widget_operation_help.item(5, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"[0-9]", None));
        ___qtablewidgetitem34 = self.table_widget_operation_help.item(5, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u81f3\u4f20\u611f\u5668[1-9]", None));
        ___qtablewidgetitem35 = self.table_widget_operation_help.item(6, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"F1", None));
        ___qtablewidgetitem36 = self.table_widget_operation_help.item(6, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362HUD\u663e\u793a", None));
        ___qtablewidgetitem37 = self.table_widget_operation_help.item(7, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"R", None));
        ___qtablewidgetitem38 = self.table_widget_operation_help.item(7, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u56fe\u50cf\u5230\u78c1\u76d8", None));
        ___qtablewidgetitem39 = self.table_widget_operation_help.item(8, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"C", None));
        ___qtablewidgetitem40 = self.table_widget_operation_help.item(8, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u5929\u6c14", None));
        ___qtablewidgetitem41 = self.table_widget_operation_help.item(9, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"V", None));
        ___qtablewidgetitem42 = self.table_widget_operation_help.item(9, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u5c42", None));
        ___qtablewidgetitem43 = self.table_widget_operation_help.item(10, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"B/SHIFT+B", None));
        ___qtablewidgetitem44 = self.table_widget_operation_help.item(10, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d/\u5378\u8f7d\u56fe\u5c42", None));
        self.table_widget_operation_help.setSortingEnabled(__sortingEnabled)

        self.line_edit_operation_help.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6377\u952e\u64cd\u4f5c\u8bf4\u660e", None))
        ___qtablewidgetitem45 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u865a\u62df\u9a7e\u9a76", None));
        ___qtablewidgetitem46 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u9a7e\u9a76", None));
        self.btn_generate_traffic.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u901a\u521d\u59cb\u5316", None))
        self.btn_manual_control.setText(QCoreApplication.translate("MainWindow", u"\u865a\u62df\u9a7e\u9a76", None))
        self.btn_automatic_control.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u9a7e\u9a76", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.btn_open_dir.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.line_edit_filenames.setText("")
        self.line_edit_filenames.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        ___qtablewidgetitem47 = self.table_widget_transform_upload_result.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"normal2fisheye", None));
        ___qtablewidgetitem48 = self.table_widget_transform_upload_result.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"cubemap2fisheye", None));
        ___qtablewidgetitem49 = self.table_widget_transform_upload_result.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272\u7ed3\u679c", None));
        ___qtablewidgetitem50 = self.table_widget_transform_upload_result.verticalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.table_widget_transform_upload_result.verticalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.table_widget_transform_upload_result.verticalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem53 = self.table_widget_transform_upload_result.verticalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem54 = self.table_widget_transform_upload_result.verticalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem55 = self.table_widget_transform_upload_result.verticalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem56 = self.table_widget_transform_upload_result.verticalHeaderItem(6)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem57 = self.table_widget_transform_upload_result.verticalHeaderItem(7)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem58 = self.table_widget_transform_upload_result.verticalHeaderItem(8)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem59 = self.table_widget_transform_upload_result.verticalHeaderItem(9)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem60 = self.table_widget_transform_upload_result.verticalHeaderItem(10)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem61 = self.table_widget_transform_upload_result.verticalHeaderItem(11)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem62 = self.table_widget_transform_upload_result.verticalHeaderItem(12)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem63 = self.table_widget_transform_upload_result.verticalHeaderItem(13)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem64 = self.table_widget_transform_upload_result.verticalHeaderItem(14)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem65 = self.table_widget_transform_upload_result.verticalHeaderItem(15)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem66 = self.table_widget_transform_upload_result.verticalHeaderItem(16)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem67 = self.table_widget_transform_upload_result.verticalHeaderItem(17)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem68 = self.table_widget_transform_upload_result.verticalHeaderItem(18)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem69 = self.table_widget_transform_upload_result.verticalHeaderItem(19)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem70 = self.table_widget_transform_upload_result.verticalHeaderItem(20)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem71 = self.table_widget_transform_upload_result.verticalHeaderItem(21)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem72 = self.table_widget_transform_upload_result.verticalHeaderItem(22)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled1 = self.table_widget_transform_upload_result.isSortingEnabled()
        self.table_widget_transform_upload_result.setSortingEnabled(False)
        self.table_widget_transform_upload_result.setSortingEnabled(__sortingEnabled1)

        self.btn_segmentation_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u56fe\u50cf\u8fdb\u884c\u5206\u5272", None))
        self.btn_segmentation_video.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u89c6\u9891\u8fdb\u884c\u5b9e\u65f6\u5206\u5272", None))
        self.btn_fisheye_one2one.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u56fe\u50cf\u8f6c\u9c7c\u773c\u56fe\u50cf", None))
        self.btn_fisheye_five2one.setText(QCoreApplication.translate("MainWindow", u"\u4e94\u5f20\u666e\u901a\u56fe\u50cf\u62fc\u63a5\u9c7c\u773c\u56fe\u50cf", None))
        self.label.setText("")
        self.label_3.setText("")
        self.btn_get_fisheye.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9c7c\u773c\u56fe\u50cf", None))
        self.btn_get_common.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5176\u4ed6\u975e\u7578\u53d8\u4f20\u611f\u5668\u56fe\u50cf", None))
        ___qtablewidgetitem73 = self.table_widget_get_image.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u9c7c\u773c\u56fe\u50cf", None));
        ___qtablewidgetitem74 = self.table_widget_get_image.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u975e\u7578\u53d8\u4f20\u611f\u5668\u56fe\u50cf", None));
        ___qtablewidgetitem75 = self.table_widget_get_image.verticalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem76 = self.table_widget_get_image.verticalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem77 = self.table_widget_get_image.verticalHeaderItem(2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem78 = self.table_widget_get_image.verticalHeaderItem(3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem79 = self.table_widget_get_image.verticalHeaderItem(4)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem80 = self.table_widget_get_image.verticalHeaderItem(5)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem81 = self.table_widget_get_image.verticalHeaderItem(6)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem82 = self.table_widget_get_image.verticalHeaderItem(7)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem83 = self.table_widget_get_image.verticalHeaderItem(8)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem84 = self.table_widget_get_image.verticalHeaderItem(9)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem85 = self.table_widget_get_image.verticalHeaderItem(10)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem86 = self.table_widget_get_image.verticalHeaderItem(11)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem87 = self.table_widget_get_image.verticalHeaderItem(12)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem88 = self.table_widget_get_image.verticalHeaderItem(13)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem89 = self.table_widget_get_image.verticalHeaderItem(14)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem90 = self.table_widget_get_image.verticalHeaderItem(15)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem91 = self.table_widget_get_image.verticalHeaderItem(16)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem92 = self.table_widget_get_image.verticalHeaderItem(17)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem93 = self.table_widget_get_image.verticalHeaderItem(18)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem94 = self.table_widget_get_image.verticalHeaderItem(19)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem95 = self.table_widget_get_image.verticalHeaderItem(20)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem96 = self.table_widget_get_image.verticalHeaderItem(21)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem97 = self.table_widget_get_image.verticalHeaderItem(22)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled2 = self.table_widget_get_image.isSortingEnabled()
        self.table_widget_get_image.setSortingEnabled(False)
        self.table_widget_get_image.setSortingEnabled(__sortingEnabled2)

        self.btn_raw_to_platte.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u4e49\u5206\u5272\u539f\u59cb\u56fe\u50cf\u8f6c\u6362\u4e3aCityscapes\u8c03\u8272\u677f\u56fe\u50cf", None))
        self.btn_send_mail.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: IngunityDrive", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v5.1.0-stable", None))
    # retranslateUi

