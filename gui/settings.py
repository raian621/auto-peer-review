from PyQt6.QtWidgets import QWidget, QLabel

class SettingsWidget(QWidget):
    def __init__(self, parent=None, setView=None):
        QWidget.__init__(self, parent)
        if setView != None:
            self.setView = setView
        QLabel("Settings", self)
        