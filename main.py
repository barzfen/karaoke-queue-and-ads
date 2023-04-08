import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':
    print("app is starting")
    app = QApplication(sys.argv)
    arg = "noflag"
    window = MainWindow()
    window.show()
    if len(sys.argv) > 1:
        if sys.argv[1] == "-f":
            window.set_fullscreen()

    sys.exit(app.exec())
