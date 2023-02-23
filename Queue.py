from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtCore import Qt
import requests


class Queue(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)

        self.setMinimumSize(1, 1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        res = requests.get("https://connectkaraoke.com/showlogin.php?ShowDirect=MZSJFQKL")
        key = res.url.split("/")[-2]
        self.proxy = f"https://connectkaraoke.com/proxy/{key}/queue"

        print(self.proxy)

        self.refresh_site()

    def refresh_site(self):
        self.load(QUrl(self.proxy))
        self.show()
