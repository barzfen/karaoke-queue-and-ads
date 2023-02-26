from Ui_MainWindow import Ui_MainWindow
from PySide6.QtCore import QTimer, Qt, QEvent
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout

from Queue import Queue
from Promotions import Promotions
from SettingsPage import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Queue and Image Display")

        ######################################
        # Set up and add the Stacked Widgets #
        ######################################
        #######################
        # Setting Page set up #
        #######################
        self.settings_page = SettingsPage(self.ui.stackedWidget)
        self.ui.stackedWidget.addWidget(self.settings_page)
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
        self.queue_view = Queue(self.ui.queue_page)
        queue_layout.addWidget(self.queue_view)

        # Redirect WebView key press events to MainWindow
        self.queue_view.focusProxy().installEventFilter(self)

        self.queue_timer = QTimer()
        self.queue_timer.setSingleShot(True)
        self.promo_timer = QTimer()
        self.queue_timer.setSingleShot(True)
        self.queue_timer.timeout.connect(self.show_promo)
        self.promo_timer.timeout.connect(self.show_queue)

        self.ui.full_screen_btn.clicked.connect(self.set_fullscreen)
        self.ui.settings_btn.clicked.connect(self.show_settings)
        self.ui.close_btn.clicked.connect(self.close)
        self.settings_page.done_signal.connect(self.settings_changed)

        # Flag so that the page doesn't change with timer
        # when you switch to the settings page
        self.showing_settings = False

        self.show_queue()

    # Required to handle key events in QWebEngineView
    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
                source.parentWidget() is self.queue_view):
            self.keyPressEvent(event)
            return False
        return super().eventFilter(source, event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            self.windowHandle().showNormal()
            self.ui.full_screen_btn.show()
            self.ui.settings_btn.show()
            self.ui.close_btn.show()

        super().keyPressEvent(event)

    def set_fullscreen(self):
        self.windowHandle().showFullScreen()
        self.ui.full_screen_btn.hide()
        self.ui.settings_btn.hide()
        self.ui.close_btn.hide()

    def show_settings(self):
        self.showing_settings = True
        self.ui.stackedWidget.setCurrentWidget(self.settings_page)

    def end_program(self):
        self.close()

    def show_queue(self):
        if not self.showing_settings:
            self.ui.stackedWidget.setCurrentWidget(self.ui.queue_page)
            self.queue_view.start_scroll()
            self.queue_timer.singleShot(5000, self.show_promo)
            self.promo_label.load_next_image()

    def show_promo(self):
        if not self.showing_settings:
            self.queue_view.stop_scrolling()
            self.ui.stackedWidget.setCurrentWidget(self.ui.promo_page)
            self.promo_timer.singleShot(5000, self.show_queue)
            self.queue_view.refresh_site()

    def settings_changed(self):
        self.showing_settings = False
        # Update of settings goes here

        self.show_queue()
