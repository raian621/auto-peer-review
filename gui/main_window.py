from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from .main_menu import MainMenu
from .reviews import ReviewsWidget
from .settings import SettingsWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        
        self.changeView = {
            'main': lambda: self.stackedWidget.setCurrentIndex(0),
            'review': lambda: self.stackedWidget.setCurrentIndex(1),
            'settings': lambda: self.stackedWidget.setCurrentIndex(2)
        }
        
        self.stackedWidget = QStackedWidget()
        self.setGeometry(50, 50, 800, 500)
        self.setCentralWidget(self.stackedWidget)
        
        setViewCallback = lambda view: self.setView(view)
        mainMenu = MainMenu(None, setViewCallback)
        self.stackedWidget.addWidget(mainMenu)
        reviewsWidget = ReviewsWidget(None, setViewCallback)
        self.stackedWidget.addWidget(reviewsWidget)
        settingsWidget = SettingsWidget(None, setViewCallback)
        self.stackedWidget.addWidget(settingsWidget)
        
    def setView(self, view):
        self.changeView[view]()