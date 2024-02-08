import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget

from .main_window import MainWindow

def start_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())