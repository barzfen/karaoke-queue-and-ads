from Ui_MainWindow import Ui_MainWindow
from Promotions import Promotions
from Queue import Queue
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Queue and Image Display")

        self.ui.full_screen_btn.clicked.connect(self.set_fullscreen)
        self.ui.settings_btn.clicked.connect(self.show_settings)
        self.ui.close_btn.clicked.connect(self.close)

        ######################################
        # Set up and add the Stacked Widgets #
        ######################################
        ######################
        # Promo Widget setup #
        ######################
        promo_layout = QHBoxLayout()
        promo_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.promo_page.setLayout(promo_layout)
        self.promo_label = Promotions(self.ui.promo_page)
        promo_layout.addWidget(self.promo_label)
        self.ui.stackedWidget.setCurrentWidget(self.ui.queue_page)
        #####################
        # Queue page set up #
        #####################
        queue_layout = QHBoxLayout()
        queue_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.queue_page.setLayout(queue_layout)
        self.queue_view = Queue(self.ui.queue_page)
        promo_layout.addWidget(self.queue_view)
        #######################
        # Setting Page set up #
        #######################

        self.ui.stackedWidget.setCurrentWidget(self.ui.queue_page)

        # self.timer = QTimer()
        # self.timerScroll = QTimer()
        # self.timer.timeout.connect(self.onTimeout)
        # self.timerScroll.timeout.connect(self.scroll_page)
        #
        # self.show_website()
        # self.timerScroll.start(100)

    def set_fullscreen(self):
        print("Set full screen goes here")

    def show_settings(self):
        print("Setting goes here")

    def end_program(self):
        self.close()

    def show_website(self):
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
        self.image_label.setPixmap(QPixmap("Images/meton2.jpg"))
        self.image_label.show()
        self.timer.start(10000)

    def onTimeout(self):
        if self.web_view.isVisible():
            self.showImage()
        else:
            self.showWebsite()

    def scroll_page(self):

        self.web_view.page().runJavaScript("window.scrollBy(0,1);")
