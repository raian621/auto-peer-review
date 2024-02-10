import sys
from PyQt6.QtWidgets import QApplication
from .main_window import MainWindow


def start_gui(config):
  app = QApplication(sys.argv)
  window = MainWindow(None, config)
  if config.members.selfName == '' and len(config.members.memberNames) == 0:
    window.setView('settings')
  window.show()
  sys.exit(app.exec())
