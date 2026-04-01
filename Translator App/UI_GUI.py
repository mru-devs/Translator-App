# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(253, 205)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 251, 171))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.SnipButton = QPushButton(self.page)
        self.SnipButton.setObjectName(u"SnipButton")
        self.SnipButton.setGeometry(QRect(10, 10, 111, 41))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(12)
        self.SnipButton.setFont(font)
        icon = QIcon()
        icon.addFile(u"SnipIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SnipButton.setIcon(icon)
        self.SnipButton.setIconSize(QSize(20, 20))
        self.SettingsButton = QPushButton(self.page)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setGeometry(QRect(130, 10, 111, 41))
        self.SettingsButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"481272.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsButton.setIcon(icon1)
        self.SettingsButton.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(10, 70, 231, 71))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.lineEdit = QLineEdit(self.page_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 30, 113, 20))
        self.label = QLabel(self.page_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 81, 21))
        self.lineEdit_2 = QLineEdit(self.page_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 0, 113, 20))
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 81, 21))
        self.stackedWidget_2.addWidget(self.page_4)
        self.buttonBox = QDialogButtonBox(self.page_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 140, 156, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.radioButton = QRadioButton(self.page_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 10, 111, 17))
        self.radioButton_2 = QRadioButton(self.page_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 40, 111, 17))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 253, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SnipButton.setText(QCoreApplication.translate("MainWindow", u"New Snip", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Insert value...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"API Frequency:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Insert value...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Google Translate", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Gemini", None))
    # retranslateUi

