from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MainMenu(QWidget):
    def __init__(self, parent=None, changeView=None):
        QWidget.__init__(self, parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        buttonGroup = QVBoxLayout()
        buttonGroup.setAlignment(Qt.AlignmentFlag.AlignTop)
        titleLabel = QLabel("Peer Review Assistant")
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(titleLabel)
        layout.addLayout(buttonGroup)
        
        startButton = QPushButton()
        startButton.setText('Start')
        startButton.clicked.connect(lambda: changeView('review'))
        buttonGroup.addWidget(startButton)
        
        settingsButton = QPushButton()
        settingsButton.setText('Settings')
        settingsButton.clicked.connect(lambda: changeView('settings'))
        buttonGroup.addWidget(settingsButton)
        
        
        