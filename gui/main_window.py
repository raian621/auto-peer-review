from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from .main_menu import MainMenu
from .reviews import ReviewsWidget
from .settings import SettingsWidget
from data import CONFIG_PATH


class MainWindow(QMainWindow):
  def __init__(self, parent=None, config=None):
    QMainWindow.__init__(self, parent)

    self.config = config
    self.setWindowTitle('Peer Review Assistant')

    self.changeView = {
      'main': lambda: self.stackedWidget.setCurrentIndex(0),
      'review': lambda: self.stackedWidget.setCurrentIndex(1),
      'settings': lambda: self.stackedWidget.setCurrentIndex(2),
    }

    self.stackedWidget = QStackedWidget()
    self.setGeometry(50, 50, 100, 800)
    self.setCentralWidget(self.stackedWidget)
    self.setContentsMargins(0, 0, 0, 0)

    setViewCallback = lambda view: self.setView(view)
    mainMenu = MainMenu(None, setViewCallback)
    self.stackedWidget.addWidget(mainMenu)
    reviewsWidget = ReviewsWidget(
      setViewCallback,
      [self.config.members.selfName, *self.config.members.memberNames]
    )
    self.reviewsWidget = reviewsWidget
    self.stackedWidget.addWidget(reviewsWidget)
    settingsWidget = SettingsWidget(
      None,
      setViewCallback,
      lambda: self.updateConfig(),
      config
    )
    self.stackedWidget.addWidget(settingsWidget)
    if config == None:
      self.setView('settings')

  def setView(self, view):
    self.changeView[view]()

  def updateConfig(self):
    self.config.save(CONFIG_PATH)
    self.reviewsWidget.setMembers([
      self.config.members.selfName,
      *self.config.members.memberNames
    ])
    self.reviewsWidget.initReviews()
