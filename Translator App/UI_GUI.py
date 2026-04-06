# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
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
        self.InsertValue_Frequency = QLineEdit(self.page_4)
        self.InsertValue_Frequency.setObjectName(u"InsertValue_Frequency")
        self.InsertValue_Frequency.setGeometry(QRect(100, 30, 113, 20))
        self.label_APIFreq = QLabel(self.page_4)
        self.label_APIFreq.setObjectName(u"label_APIFreq")
        self.label_APIFreq.setGeometry(QRect(10, 30, 81, 21))
        self.InsertValue_Key = QLineEdit(self.page_4)
        self.InsertValue_Key.setObjectName(u"InsertValue_Key")
        self.InsertValue_Key.setGeometry(QRect(100, 0, 113, 20))
        self.InsertValue_Key.setClearButtonEnabled(False)
        self.label_APIKey = QLabel(self.page_4)
        self.label_APIKey.setObjectName(u"label_APIKey")
        self.label_APIKey.setGeometry(QRect(10, 0, 81, 21))
        self.stackedWidget_2.addWidget(self.page_4)
        self.saveSettingsButtons = QDialogButtonBox(self.page_2)
        self.saveSettingsButtons.setObjectName(u"saveSettingsButtons")
        self.saveSettingsButtons.setGeometry(QRect(50, 140, 156, 23))
        self.saveSettingsButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.GoogleTranslateButton = QRadioButton(self.page_2)
        self.GoogleTranslateButton.setObjectName(u"GoogleTranslateButton")
        self.GoogleTranslateButton.setGeometry(QRect(10, 10, 111, 17))
        self.GeminiButton = QRadioButton(self.page_2)
        self.GeminiButton.setObjectName(u"GeminiButton")
        self.GeminiButton.setGeometry(QRect(10, 40, 111, 17))
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

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SnipButton.setText(QCoreApplication.translate("MainWindow", u"New Snip", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.InsertValue_Frequency.setText("")
        self.InsertValue_Frequency.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a value...", None))
        self.label_APIFreq.setText(QCoreApplication.translate("MainWindow", u"API Frequency:", None))
        self.InsertValue_Key.setText("")
        self.InsertValue_Key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a value...", None))
        self.label_APIKey.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.GoogleTranslateButton.setText(QCoreApplication.translate("MainWindow", u"Google Translate", None))
        self.GeminiButton.setText(QCoreApplication.translate("MainWindow", u"Gemini", None))
    # retranslateUi

