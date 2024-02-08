from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from .main_menu import MainMenu
from .reviews import ReviewsWidget
from .settings import SettingsWidget
from config import save_config


class MainWindow(QMainWindow):
  def __init__(self, parent=None, config=None):
    QMainWindow.__init__(self, parent)

    self.config = config
    self.setWindowTitle('Peer Review Assistant')

    self.changeView = {
      'main': lambda: self.stackedWidget.setCurrentIndex(0),
      'review': lambda: self.stackedWidget.setCurrentIndex(1),
      'settings': lambda: self.stackedWidget.setCurrentIndex(2)
    }

    self.stackedWidget = QStackedWidget()
    self.setGeometry(50, 50, 800, 500)
    self.setCentralWidget(self.stackedWidget)
    self.setContentsMargins(0, 0, 0, 0)

    setViewCallback = lambda view: self.setView(view)
    mainMenu = MainMenu(None, setViewCallback)
    self.stackedWidget.addWidget(mainMenu)
    reviewsWidget = ReviewsWidget(None, setViewCallback)
    self.stackedWidget.addWidget(reviewsWidget)
    settingsWidget = SettingsWidget(
      None,
      setViewCallback,
      lambda: self.updateConfig(),
      config
    )
    self.stackedWidget.addWidget(settingsWidget)
    if config != None:
      reviewsWidget.setMembers(config['members'])
    else:
      self.setView('settings')

  def setView(self, view):
    self.changeView[view]()

  def updateConfig(self):
    save_config(self.config)
