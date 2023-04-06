from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QSettings
from Ui_SettingsPage import Ui_SettingsPage


class SettingsPage(QWidget):

    done_signal = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_SettingsPage()
        self.ui.setupUi(self)

        self.settings = QSettings('FensomSoftware', 'KaraokeQueue')

        if not self.settings.contains('Access/key'):
            self.settings.setValue('Access/key', '')

        if not self.settings.contains('Timing/queue'):
            self.settings.setValue('Timing/queue', 50)

        if not self.settings.contains('Timing/promo'):
            self.settings.setValue('Timing/promo', 25)

        self.load_values()

        self.ui.apply_btn.clicked.connect(self.apply_changes)
        self.ui.cancel_btn.clicked.connect(self.cancel_changes)

    def apply_changes(self):
        self.settings.setValue('Access/key', self.ui.webkey_edit.text())
        self.settings.setValue('Timing/queue', self.ui.queue_time_spinbox.value())
        self.settings.setValue('Timing/promo', self.ui.promo_time_spinbox.value())
        self.done_signal.emit()
        print("applied changes")

    def get_settings(self):
        settings = dict()
        settings['access_key'] = self.settings.value('Access/key')
        settings['queue_time'] = int(self.settings.value('Timing/queue')) * 1000
        settings['promo_time'] = int(self.settings.value('Timing/promo')) * 1000

        return settings

    def cancel_changes(self):
        self.load_values()
        self.done_signal.emit()

    def load_values(self):
        self.ui.webkey_edit.setText(self.settings.value('Access/key'))
        self.ui.queue_time_spinbox.setValue(int(self.settings.value('Timing/queue')))
        self.ui.promo_time_spinbox.setValue(int(self.settings.value('Timing/promo')))
