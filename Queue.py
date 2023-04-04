import requests
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractSlider, QAbstractItemView
from api_calls.getQueue import getQueue #, getCurrentSinger

from Ui_Queue import Ui_Queue


class Queue(QWidget):
    def __init__(self, parent, access_key):
        super().__init__(parent)

        self.ui = Ui_Queue()
        self.ui.setupUi(self)
        self.ui.queue_table.verticalHeader().setVisible(False)

        #self.ui.queue_table.horizontalHeaderItem(2).setText("Song")
        #elf.ui.queue_table.horizontalHeaderItem(3).setText("Approx Time")

        self.refresh_interval = 20000  # 20 seconds
        self.refresh_timer = QTimer()

        res = requests.get(f"https://connectkaraoke.com/showlogin.php?ShowDirect={access_key}")
        self.key = res.url.split("/")[-2]

        self.scroll_timer = QTimer()
        self.scroll_timer.timeout.connect(self.scroll_down)
        self.scrolling = False
        self.refresh_timer.start(self.refresh_interval)
        self.refresh_list()
        self.start_scroll()

    def refresh_list(self):
        queue_list = getQueue(self.key)
        # current_singer = getCurrentSinger()
        # self.ui.bio.setText(f"{current_singer[0]} {current_singer[1]} {current_singer[2]}")
        table = self.ui.queue_table
        table.clear()
        table.setRowCount(0)
        for row in queue_list:
            row_pos = table.rowCount()
            table.insertRow(row_pos)
            table.setItem(row_pos, 0, QTableWidgetItem(row['singername']))
            table.setItem(row_pos, 1, QTableWidgetItem(row['songname']))
            table.setItem(row_pos, 2, QTableWidgetItem(row['estimatedtime']))
        self.refresh_timer.singleShot(self.refresh_interval, self.refresh_list)

    def start_scroll(self):
        self.scrolling = True
        self.scroll_down()

    def stop_scrolling(self):
        self.scrolling = False

    def scroll_down(self):
        if self.scrolling:
            scrollbar = self.ui.queue_table.verticalScrollBar()
            scrollbar.setValue(scrollbar.value() + 1)
            self.scroll_timer.singleShot(100, self.scroll_down)

            if scrollbar.value() >= scrollbar.maximum():
                scrollbar.setValue(0)
