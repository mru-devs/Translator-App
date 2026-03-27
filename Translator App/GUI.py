from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPainter, QColor
import numpy as np

import ScreenMSS
import translator
class SnippedArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.area = None
        self.coordinates = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
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
        if(self.snippedObject is not None):
            self.snippedObject.close()
            self.snippedObject.deleteLater()
            self.snippedObject = None


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
                

class WindowWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        labelScreen2 = QLabel()

        ScreenBarButton = QPushButton("✂ New")
        ScreenBarButton.clicked.connect(self.startSnipping)

        menuWidget = QWidget()
        menuLayout = QHBoxLayout(menuWidget)
        menuLayout.addWidget(ScreenBarButton, 1)
        menuLayout.addWidget(labelScreen2, 10)

        temp = QLabel('Temporary text')
        temp.setAlignment(Qt.AlignCenter)
        tempWidget = QWidget()
        tempLayout = QVBoxLayout(tempWidget)
        tempLayout.addWidget(temp)
    
        
        windowLayout = QVBoxLayout(self)
        windowLayout.addWidget(menuWidget, 1)
        windowLayout.addWidget(tempWidget, 15)


        self.snippingWindow = SnippingMode()
    def startSnipping(self):
        self.snippingWindow.startWidget()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window')
        self.setFixedSize(800, 600)

        self.setCentralWidget(WindowWidget())

        
application = QApplication()

window = MainWindow()
window.show()

application.exec()

