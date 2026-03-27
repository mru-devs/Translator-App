from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor
import numpy as np

#import ScreenMSS
#import main

class SnippingMode(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)
        self.setWindowOpacity(0.5)
        self.showFullScreen()
        
        self.positionStart = None
        self.positionEnd = None

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
            #x1,y1,x2,y2 = QRect(self.positionStart, self.positionEnd).normalized().getCoords()
            #ScreenMSS.ScreenShotter(x1,y1,x2,y2)

            #appTranslate = main.functionTranslate()
            #appTranslate.JapaneseToEnglish(ScreenMSS.filePathName)


    def paintEvent(self, event):
        draggedArea = QPainter(self)
        draggedArea.fillRect(self.rect(), QColor(0, 0, 0, 100))
        if self.positionStart is not None:
            area = QRect(self.positionStart, self.positionEnd).normalized()
            draggedArea.fillRect(area, QColor(255, 255, 255, 255))
            draggedArea.setPen(Qt.green)
            draggedArea.drawRect(area)

    

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

    def startSnipping(self):
        self.snippingWindow = SnippingMode()
        #self.snippingWindow.show()



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

