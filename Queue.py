import requests
from PySide6.QtCore import QUrl, QTimer, Qt


from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

from api_calls.getQueue import getQueue


class Queue(QWidget):
    def __init__(self, parent, access_key):
        super().__init__(parent)

        self.setMinimumSize(1, 1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.refresh_interval = 20000  # 20 seconds
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_list)

        res = requests.get(f"https://connectkaraoke.com/showlogin.php?ShowDirect={access_key}")
        self.key = res.url.split("/")[-2]
        #self.queue_list = getQueue(self.key)
        self.queue_widget = QListWidget()
        self.queue_widget.setSortingEnabled(False)
        self.queue_widget.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(self.queue_widget)
        self.setLayout(layout)

        self.setMinimumSize(1, 1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.scroll_timer = QTimer()
        self.refresh_timer.start(self.refresh_interval)
        #self.scroll_timer.timeout.connect(self.scroll_down)




        self.show()

    def refresh_list(self):
        queue_list = getQueue(self.key)
        self.queue_widget.clear()

        for song in queue_list:

            item = QListWidgetItem(f"{song['singername']} - {song['songname']} ({song['estimatedtime']})")
            self.queue_widget.addItem(item)
            

        self.queue_widget.setCurrentRow(0)