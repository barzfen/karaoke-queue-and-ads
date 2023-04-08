import time
import requests
from PySide6.QtGui import QFont, QPalette
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from api_calls.getQueue import getQueue, getCurrentSinger
from PySide6.QtCore import Qt, QTimer, QThread, Signal, Slot


from Ui_Queue import Ui_Queue


class Queue(QWidget):
    def __init__(self, parent, access_key):
        super().__init__(parent)

        self.ui = Ui_Queue()
        self.ui.setupUi(self)
        header_font = QFont("Arial", 30)
        self.ui.queue_table.horizontalHeader().setFont(header_font)


        self.top_queue_wait_time = 4000  # 4 seconds
        self.bottom_queue_wait_time = 2000  # 2 seconds
        self.refresh_timer = QTimer()

        self.current_singer = {}
        self.queue_list = {}

        self.access_key = access_key
        self.key = None
        self.update_thread = DataUpdateThread(access_key)
        self.update_thread.data_retrieved.connect(self.update_data)
        self.update_thread.start()

        self.scroll_timer = QTimer()
        self.refresh_list()

    def refresh_list(self):
        self.ui.queue_table.verticalScrollBar().setValue(0)
        if len(self.current_singer) > 0:
            self.ui.banner.setText(f"Current Singer: {self.current_singer['stageName']}")
            self.ui.bio.setText(self.current_singer['bio'])
        singer_font = QFont('Noto Color Emoji', 30)
        self.ui.banner.setFont(singer_font)
        singer_font.setPointSize(20)
        self.ui.bio.setFont(singer_font)
        table = self.ui.queue_table
        table.clear()
        self.ui.queue_table.setColumnCount(3)
        self.ui.queue_table.setHorizontalHeaderLabels(["Est. Time", "Name", "Song"])
        self.ui.queue_table.horizontalHeader().setStyleSheet("QHeaderView::section {color: white; background-color: black}")
        table.setRowCount(0)
        if len(self.queue_list) > 0:
            for row in self.queue_list:
                row_pos = table.rowCount()
                table.insertRow(row_pos)
                table.setItem(row_pos, 0, QTableWidgetItem(row['estimatedtime']))
                table.setItem(row_pos, 1, QTableWidgetItem(row['singername']))
                table.setItem(row_pos, 2, QTableWidgetItem(row['songname']))
                fnt = QFont('Arial', 28)
                for i in range(3):
                    curr_cell = table.item(row_pos, i)
                    curr_cell.setFont(fnt)
                table.setItem(0, 0, QTableWidgetItem("NEXT"))
                table.item(0, 0).setFont(fnt)
            table.resizeRowsToContents()
            table.setAlternatingRowColors(True)
            table.setStyleSheet("""
                alternate-background-color: rgb(192, 192, 192); background-color: rgb(222, 211, 202);
                QTableWidget::item {border: 6px};
            """)

            self.scroll_timer.singleShot(self.top_queue_wait_time, self.scroll_down)# Wait 2 seconds before scrolling
        else:
            print("Queue not yet loaded, trying again in 2 seconds")
            self.refresh_timer.singleShot(2000, self.refresh_list)

    def scroll_down(self):
        scrollbar = self.ui.queue_table.verticalScrollBar()
        scrollbar.setValue(scrollbar.value() + 1)

        if scrollbar.value() >= scrollbar.maximum():
            self.refresh_timer.singleShot(self.bottom_queue_wait_time, self.refresh_list)
        else:
            self.scroll_timer.singleShot(100, self.scroll_down)

    @Slot(dict)
    def update_data(self, data):
        self.current_singer = data["current_singer"]
        self.queue_list = data["queue_list"]


class DataUpdateThread(QThread):
    data_retrieved = Signal(dict)

    def __init__(self, access_key):
        super().__init__()
        self.access_key = access_key
        self.key = ""

    def run(self):
        res = requests.get(f"https://connectkaraoke.com/showlogin.php?ShowDirect={self.access_key}")
        self.key = res.url.split("/")[-2]

        while True:
            queue_list = getQueue(self.key)
            current_singer_json = getCurrentSinger()
            current_singer = current_singer_json['data']['getCurrentSinger']
            song_data = {"queue_list": queue_list, "current_singer": current_singer}
            self.data_retrieved.emit(song_data)
            time.sleep(15)
