import requests
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView


class Queue(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)

        self.setMinimumSize(1, 1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        res = requests.get("https://connectkaraoke.com/showlogin.php?ShowDirect=MZSJFQKL")
        key = res.url.split("/")[-2]
        self.proxy = f"https://connectkaraoke.com/proxy/{key}/queue"
        self.refresh_site()

        self.scroll_timer = QTimer()
        self.scroll_timer.timeout.connect(self.scroll_down)
        self.scrolling = False

    def refresh_site(self):
        self.load(QUrl(self.proxy))
        self.page().runJavaScript("window.scrollTo(0, 0);")

        self.show()

    def start_scroll(self):
        self.scrolling = True
        self.scroll_down()

    def stop_scrolling(self):
        self.scrolling = False

    def scroll_down(self):
        if self.scrolling:
            self.page().runJavaScript("window.scrollBy(0,1);")
            self.scroll_timer.singleShot(100, self.scroll_down)

