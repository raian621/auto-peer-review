import sys
from PyQt6.QtWidgets import QApplication
from .main_window import MainWindow


def start_gui(config):
  print(config)
  app = QApplication(sys.argv)
  window = MainWindow(None, config)
  window.show()
  sys.exit(app.exec())
