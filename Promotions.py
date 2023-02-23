import os
from glob import glob
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QSizePolicy


class Promotions(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setMinimumSize(1, 1)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Load images
        file_path = os.path.join(os.getcwd(), "Images")

        self.file_names = []
        for extension in [
                             os.path.join(file_path, "*.png"),
                             os.path.join(file_path, "*.jpg"),
                             os.path.join(file_path, "*.jpeg")
                         ]:
            for file in glob(extension):
                self.file_names.append(os.path.join(file_path, file))

        self.file_index = 0
        self.current_image = QPixmap(self.file_names[self.file_index])

        self.load_image()

    def resizeEvent(self, event):
        self.load_image()

    def load_image(self):
        self.setPixmap(self.current_image.scaled(self.frameSize(), Qt.KeepAspectRatio))
        self.setScaledContents(True)

    def load_next_image(self):
        self.file_index += 1
        self.file_index %= len(self.file_names)
        self.current_image = QPixmap(self.file_names[self.file_index])
        self.load_image()
