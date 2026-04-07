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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(515, 338)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 511, 231))
        self.pageMain = QWidget()
        self.pageMain.setObjectName(u"pageMain")
        self.SnipButton = QPushButton(self.pageMain)
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
        self.SettingsButton = QPushButton(self.pageMain)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setGeometry(QRect(130, 10, 111, 41))
        self.SettingsButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"481272.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsButton.setIcon(icon1)
        self.SettingsButton.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.pageMain)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.verticalLayoutWidget = QWidget(self.pageSettings)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 111, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_SnipMode = QPushButton(self.verticalLayoutWidget)
        self.pushButton_SnipMode.setObjectName(u"pushButton_SnipMode")

        self.verticalLayout.addWidget(self.pushButton_SnipMode)

        self.pushButton_TranslationSettings = QPushButton(self.verticalLayoutWidget)
        self.pushButton_TranslationSettings.setObjectName(u"pushButton_TranslationSettings")

        self.verticalLayout.addWidget(self.pushButton_TranslationSettings)

        self.pushButton_LanguageSettings = QPushButton(self.verticalLayoutWidget)
        self.pushButton_LanguageSettings.setObjectName(u"pushButton_LanguageSettings")

        self.verticalLayout.addWidget(self.pushButton_LanguageSettings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidgetSettings = QStackedWidget(self.pageSettings)
        self.stackedWidgetSettings.setObjectName(u"stackedWidgetSettings")
        self.stackedWidgetSettings.setGeometry(QRect(120, 0, 281, 201))
        self.pageSnippingSettings = QWidget()
        self.pageSnippingSettings.setObjectName(u"pageSnippingSettings")
        self.gridLayoutWidget = QWidget(self.pageSnippingSettings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 271, 101))
        self.horizontalLayout = QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButtonRealtime = QRadioButton(self.gridLayoutWidget)
        self.radioButtonRealtime.setObjectName(u"radioButtonRealtime")

        self.horizontalLayout.addWidget(self.radioButtonRealtime)

        self.radioButtonSingleFrame = QRadioButton(self.gridLayoutWidget)
        self.radioButtonSingleFrame.setObjectName(u"radioButtonSingleFrame")

        self.horizontalLayout.addWidget(self.radioButtonSingleFrame)

        self.stackedWidgetSettings.addWidget(self.pageSnippingSettings)
        self.pageTranslationSettings = QWidget()
        self.pageTranslationSettings.setObjectName(u"pageTranslationSettings")
        self.GoogleTranslateButton = QRadioButton(self.pageTranslationSettings)
        self.GoogleTranslateButton.setObjectName(u"GoogleTranslateButton")
        self.GoogleTranslateButton.setGeometry(QRect(20, 20, 111, 17))
        self.GeminiButton = QRadioButton(self.pageTranslationSettings)
        self.GeminiButton.setObjectName(u"GeminiButton")
        self.GeminiButton.setGeometry(QRect(20, 50, 111, 17))
        self.stackedWidgetGemini = QStackedWidget(self.pageTranslationSettings)
        self.stackedWidgetGemini.setObjectName(u"stackedWidgetGemini")
        self.stackedWidgetGemini.setGeometry(QRect(20, 80, 221, 51))
        self.pageEmpty = QWidget()
        self.pageEmpty.setObjectName(u"pageEmpty")
        self.stackedWidgetGemini.addWidget(self.pageEmpty)
        self.pageActive = QWidget()
        self.pageActive.setObjectName(u"pageActive")
        self.label_APIKey = QLabel(self.pageActive)
        self.label_APIKey.setObjectName(u"label_APIKey")
        self.label_APIKey.setGeometry(QRect(0, 0, 81, 21))
        self.label_APIFreq = QLabel(self.pageActive)
        self.label_APIFreq.setObjectName(u"label_APIFreq")
        self.label_APIFreq.setGeometry(QRect(0, 30, 81, 21))
        self.InsertValue_Key = QLineEdit(self.pageActive)
        self.InsertValue_Key.setObjectName(u"InsertValue_Key")
        self.InsertValue_Key.setGeometry(QRect(90, 0, 113, 20))
        self.InsertValue_Key.setClearButtonEnabled(False)
        self.InsertValue_Frequency = QLineEdit(self.pageActive)
        self.InsertValue_Frequency.setObjectName(u"InsertValue_Frequency")
        self.InsertValue_Frequency.setGeometry(QRect(90, 30, 113, 20))
        self.stackedWidgetGemini.addWidget(self.pageActive)
        self.stackedWidgetSettings.addWidget(self.pageTranslationSettings)
        self.pageLanguageSettings = QWidget()
        self.pageLanguageSettings.setObjectName(u"pageLanguageSettings")
        self.stackedWidgetSettings.addWidget(self.pageLanguageSettings)
        self.saveSettingsButtons = QDialogButtonBox(self.pageSettings)
        self.saveSettingsButtons.setObjectName(u"saveSettingsButtons")
        self.saveSettingsButtons.setGeometry(QRect(170, 160, 156, 23))
        self.saveSettingsButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.stackedWidget.addWidget(self.pageSettings)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 515, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidgetSettings.setCurrentIndex(0)
        self.stackedWidgetGemini.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SnipButton.setText(QCoreApplication.translate("MainWindow", u"New Snip", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_SnipMode.setText(QCoreApplication.translate("MainWindow", u"Snipping Settings", None))
        self.pushButton_TranslationSettings.setText(QCoreApplication.translate("MainWindow", u"Translation Settings", None))
        self.pushButton_LanguageSettings.setText(QCoreApplication.translate("MainWindow", u"Language Settings", None))
        self.radioButtonRealtime.setText(QCoreApplication.translate("MainWindow", u"Real-time Translation", None))
        self.radioButtonSingleFrame.setText(QCoreApplication.translate("MainWindow", u"Single-frame Translation", None))
        self.GoogleTranslateButton.setText(QCoreApplication.translate("MainWindow", u"Google Translate", None))
        self.GeminiButton.setText(QCoreApplication.translate("MainWindow", u"Gemini", None))
        self.label_APIKey.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.label_APIFreq.setText(QCoreApplication.translate("MainWindow", u"API Frequency:", None))
        self.InsertValue_Key.setText("")
        self.InsertValue_Key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a value...", None))
        self.InsertValue_Frequency.setText("")
        self.InsertValue_Frequency.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a value...", None))
    # retranslateUi

