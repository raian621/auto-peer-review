from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class MemberWidget(QWidget):
  def __init__(self, parent=None, removeMember=None, name=None):
    if removeMember != None:
      self.removeMember = removeMember
    if name != None:
      self.name = name
    else:
      self.name = ''

    layout = QHBoxLayout()
    nameInput = QLineEdit()
    nameInput.placeholderText('Enter name here')
    nameInput.textChanged.connect(set)
    layout.addWidget(nameInput)


class SettingsWidget(QScrollArea):
  def __init__(
    self,
    parent=None,
    setView=None,
    updateConfig=None,
    config=None
  ):
    QWidget.__init__(self, parent)
    self.setView = setView
    self.updateConfig = updateConfig
    self.config = config
    self.configCopy = config.copy()
    self.setupUI()

  def setupUI(self):
    layout = QVBoxLayout()
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(20)
    self.setLayout(layout)
    header = QHBoxLayout()
    body = QVBoxLayout()
    footer = QHBoxLayout()
    layout.addLayout(header)
    layout.addLayout(body)
    layout.addLayout(footer)
    header.setAlignment(Qt.AlignmentFlag.AlignTop)
    footer.setAlignment(Qt.AlignmentFlag.AlignBottom)

    backButton = QPushButton()
    backButton.setText('Back to menu')
    backButton.clicked.connect(lambda: self.setView('main'))
    header.addWidget(backButton)
    titleLabel = QLabel('Settings')
    header.addWidget(titleLabel)

    body.addWidget(QLabel('Your name:'))
    selfNameInput = QLineEdit()
    selfNameInput.setPlaceholderText('Enter your name')
    selfNameInput.setText(self.configCopy['members'].get('self', ''))
    body.addWidget(selfNameInput)
    body.addWidget(QLabel('Group member names:'))

    saveButton = QPushButton()
    saveButton.setText('Save settings')
    resetButton = QPushButton()
    resetButton.setText('Reset settings')
    footer.addWidget(saveButton)
    footer.addWidget(resetButton)
