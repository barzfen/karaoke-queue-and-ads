import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':
    print("app is starting")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
