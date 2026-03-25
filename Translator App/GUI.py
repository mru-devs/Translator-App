from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
import numpy as np


class SnippingMode(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.start = None
        self.end = None

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowFullScreen)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)
        
    
    

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
        self.snippingWindow.show()



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

