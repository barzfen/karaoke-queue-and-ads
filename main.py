import sys

import requests as requests
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, \
    QGraphicsOpacityEffect
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        res = requests.get("https://connectkaraoke.com/showlogin.php?ShowDirect=MZSJFQKL")
        items = res.url.split("/")
        self.proxy = f"https://connectkaraoke.com/proxy/{items[-2]}/queue"

        self.setWindowTitle("Website and Image Display")
        self.resize(800, 600)

        self.web_view = QWebEngineView()
        self.image_label = QLabel()
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.close)

       # self.web_view.setGraphicsEffect(QGraphicsOpacityEffect(self.web_view))
        # self.image_label.setGraphicsEffect(QGraphicsOpacityEffect(self.image_label))

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.image_label)
        layout.addWidget(self.stop_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.timer = QTimer()
        self.timerScroll = QTimer()
        self.timer.timeout.connect(self.onTimeout)
        self.timerScroll.timeout.connect(self.scroll_page)

        self.showWebsite()
        self.timerScroll.start(100)

    def showWebsite(self):
        print("we are showing queue again")
        self.image_label.hide()
        self.web_view.load(QUrl(self.proxy))
        self.web_view.show()
        self.timerScroll.start(100)
        self.timer.start(20000)

    def showImage(self):
        print("we are now showing image")
        self.web_view.hide()
        # swap out meton.jpg with your advertising image
        self.image_label.setPixmap(QPixmap("meton2.jpg"))
        self.image_label.show()
        self.timer.start(10000)

    def onTimeout(self):
        if self.web_view.isVisible():
            self.showImage()
        else:
            self.showWebsite()

    def scroll_page(self):

        self.web_view.page().runJavaScript("window.scrollBy(0,1);")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())

