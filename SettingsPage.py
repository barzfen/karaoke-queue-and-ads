from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from Ui_SettingsPage import Ui_SettingsPage


class SettingsPage(QWidget):

    done_signal = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_SettingsPage()
        self.ui.setupUi(self)

        self.ui.apply_btn.clicked.connect(self.apply_changes)

    def apply_changes(self):
        self.done_signal.emit()
