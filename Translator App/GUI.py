from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPainter, QColor

import ScreenMSS
import translator
import SettingsValues
from UI_GUI import Ui_MainWindow

class SettingsMode(QWidget):
    def __init__(self, GUI, parent=None):
        super().__init__(parent)
        self.GUI = GUI
        self.GUI.GoogleTranslateButton.clicked.connect(self.GoogleTranslateButtonPressed)
        self.GUI.GeminiButton.clicked.connect(self.GeminiButtonPressed)
        self.GUI.saveSettingsButtons.accepted.connect(self.saveSettingsOK)
        self.GUI.saveSettingsButtons.rejected.connect(self.saveSettingsCancel)
        self.temporarySettings = SettingsValues.SettingsMode()
    
    def GoogleTranslateButtonPressed(self):
        self.temporarySettings.translationMode = 'GoogleTranslate'
        self.GUI.stackedWidget_2.setCurrentIndex(0)
    
    def GeminiButtonPressed(self):
        self.temporarySettings.translationMode = 'GeminiTranslate'
        self.GUI.stackedWidget_2.setCurrentIndex(1)
    
    def saveSettingsOK(self):
        if self.GUI.stackedWidget_2.currentIndex() == 1:
            if not self.GUI.InsertValue_Key.text() or not self.GUI.InsertValue_Frequency.text():
                print("Inputs cannot be empty! Please enter a value!")
                return
            elif not self.GUI.InsertValue_Frequency.text().isdigit():
                print("Please enter a valid frequency value!")
                return
            else:
                self.temporarySettings.keyAPI = self.GUI.InsertValue_Key.text()
                self.temporarySettings.frequencyAPI = int(self.GUI.InsertValue_Frequency.text())
        SettingsValues.settings = SettingsValues.copy.copy(self.temporarySettings)

    def saveSettingsCancel(self):
        self.GUI.stackedWidget.setCurrentIndex(0)

    def loadSettings(self):
        if SettingsValues.settings.translationMode == 'GoogleTranslate':
            self.GUI.GoogleTranslateButton.setChecked(True)
            self.GoogleTranslateButtonPressed()
        elif SettingsValues.settings.translationMode == "GeminiTranslate":
            self.GUI.GeminiButton.setChecked(True)
            self.GeminiButtonPressed()
        
        self.GUI.InsertValue_Key.setText(SettingsValues.settings.keyAPI)
        self.GUI.InsertValue_Frequency.setText(str(SettingsValues.settings.frequencyAPI))

class SnippedArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.area = None
        self.coordinates = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowOpacity(0.1)
        self.showFullScreen()

        self.timer = QTimer()
        self.timer.timeout.connect(self.callMSS)
        self.timer.start(1000)

    def callMSS(self):
        x1,y1,x2,y2 = self.coordinates
        ScreenMSS.ScreenShotter(x1,y1,x2,y2)
        appTranslate = translator.functionTranslate()
        appTranslate.JapaneseToEnglish(ScreenMSS.filePathName)

    def getCoords(self, area, coords):
        self.area = area
        self.coordinates = coords
        self.update()
        self.show()
    
    def paintEvent(self, event):
        draggedArea = QPainter(self)
        draggedArea.fillRect(self.area, QColor(255, 255, 255, 255))
        draggedArea.setPen(Qt.green)
        draggedArea.drawRect(self.area)

class SnippingMode(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)
        self.setWindowOpacity(0.5)
        self.snippedObject = None
    
    def startWidget(self):
        self.positionStart = None
        self.positionEnd = None
        self.area = None
        self.showFullScreen()
        self.closeWidget()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.positionStart = event.position().toPoint()
            self.positionEnd = event.position().toPoint()
            self.update()

    def mouseMoveEvent(self, event):
        if self.positionStart is not None:
            self.positionEnd = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.positionEnd = event.position().toPoint()
            self.close()
            self.snippedObject = SnippedArea()
            self.snippedObject.getCoords(self.area, QRect(self.positionStart, self.positionEnd).normalized().getCoords())

    def paintEvent(self, event):
        draggedArea = QPainter(self)
        draggedArea.fillRect(self.rect(), QColor(0, 0, 0, 100))
        if self.positionStart is not None:
            self.area = QRect(self.positionStart, self.positionEnd).normalized()
            draggedArea.fillRect(self.area, QColor(255, 255, 255, 255))
            draggedArea.setPen(Qt.green)
            draggedArea.drawRect(self.area)

    def closeWidget(self):
        if(self.snippedObject is not None):
            self.snippedObject.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.GUI = Ui_MainWindow()
        self.GUI.setupUi(self)
        self.GUI.stackedWidget.setCurrentIndex(0)
        self.snippingWidget = SnippingMode()
        self.GUI.SnipButton.clicked.connect(self.snipButton)
        self.GUI.SettingsButton.clicked.connect(self.settingsButton)
    def snipButton(self):
        self.snippingWidget.startWidget()

        
    def settingsButton(self):
        self.settingsWidget = SettingsMode(self.GUI)
        self.GUI.stackedWidget.setCurrentIndex(1)
        self.settingsWidget.loadSettings()
    def closeEvent(self, event):
        self.snippingWidget.closeWidget()
        return super().closeEvent(event)

        
application = QApplication()

window = MainWindow()
window.show()

application.exec()