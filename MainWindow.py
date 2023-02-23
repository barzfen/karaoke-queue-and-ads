from Ui_MainWindow import Ui_MainWindow
from Promotions import Promotions
from Queue import Queue
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout


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
        queue_layout = QVBoxLayout()
        queue_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.queue_page.setLayout(queue_layout)
        self.queue_view = Queue(None)
        # self.queue_view = Queue(self.ui.queue_page)
        queue_layout.addWidget(self.queue_view)
        #######################
        # Setting Page set up #
        #######################

        self.queue_timer = QTimer()
        self.promo_timer = QTimer()
        self.queue_timer.timeout.connect(self.show_promo)
        self.promo_timer.timeout.connect(self.show_queue)

        self.show_queue()

    def set_fullscreen(self):
        print("Set full screen goes here")

    def show_settings(self):
        print("Setting goes here")

    def end_program(self):
        self.close()

    def show_queue(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.queue_page)
        self.queue_view.start_scroll()
        self.queue_timer.singleShot(5000, self.show_promo)
        self.promo_label.load_next_image()

    def show_promo(self):
        self.queue_view.stop_scrolling()
        self.ui.stackedWidget.setCurrentWidget(self.ui.promo_page)
        self.promo_timer.singleShot(5000, self.show_queue)
        self.queue_view.refresh_site()
