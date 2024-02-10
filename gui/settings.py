from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class MemberWidget(QWidget):
  def __init__(
    self,
    removeMember,
    name,
    index,
    parent=None
  ):
    QWidget.__init__(self, parent)
    self.removeMember = removeMember
    self.name = name
    self.index = index

    layout = QHBoxLayout()
    self.setLayout(layout)
    layout.setContentsMargins(0, 0, 0, 0)
    nameInput = QLineEdit()
    nameInput.setText(name)
    nameInput.setPlaceholderText('Enter name here')
    nameInput.textChanged[str].connect(self.setName)
    self.nameInput = nameInput
    layout.addWidget(nameInput)
    removeButton = QPushButton()
    removeButton.setText('Remove')
    removeButton.clicked.connect(self.remove)
    layout.addWidget(removeButton)

  def setIndex(self, index):
    self.index = index

  def setName(self, name):
    self.name = name

  def remove(self):
    self.removeMember(self.index)


class MemberWidgetGroup(QWidget):
  def __init__(
    self,
    memberNames,
    parent=None
  ):
    QWidget.__init__(self, parent)

    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(layout)

    self.memberWidgets = [
      MemberWidget(
        removeMember=self.removeName,
        name=name,
        index=i
      ) for i, name in enumerate(memberNames)
    ]

    for memberWidget in self.memberWidgets:
      layout.addWidget(memberWidget)

  def memberNames(self):
    return [memberWidget.name for memberWidget in self.memberWidgets]

  def updateName(self, name, index):
    self.memberWidgets[index].name = name

  def removeName(self, index):
    self.layout().removeWidget(self.memberWidgets[index])
    self.memberWidgets = (
      self.memberWidgets[:index] + self.memberWidgets[index + 1:]
    )

    for i in range(index, len(self.memberWidgets)):
      self.memberWidgets[i].index = i

  def addName(self):
    self.memberWidgets.append(
      MemberWidget(
        removeMember=self.removeName,
        name='',
        index=len(self.memberWidgets)
      )
    )
    self.layout().addWidget(self.memberWidgets[-1])


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
    selfNameInput.setText(self.config.members.selfName)
    self.selfNameInput = selfNameInput
    body.addWidget(selfNameInput)
    body.addWidget(QLabel('Group member names:'))
    memberWidgetGroup = MemberWidgetGroup(
      memberNames=self.config.members.memberNames
    )
    self.memberWidgetGroup = memberWidgetGroup
    body.addWidget(memberWidgetGroup)
    addMemberButton = QPushButton()
    addMemberButton.setText('Add member')
    addMemberButton.clicked.connect(self.addMember)
    body.addWidget(addMemberButton)

    saveButton = QPushButton()
    saveButton.setText('Save settings')
    saveButton.clicked.connect(self.applyConfig)
    resetButton = QPushButton()
    resetButton.setText('Reset settings')
    resetButton.clicked.connect(self.setInputFields)

    footer.addWidget(saveButton)
    footer.addWidget(resetButton)

  def applyConfig(self):
    self.config.members.selfName = self.selfNameInput.text()
    self.config.members.memberNames = self.memberWidgetGroup.memberNames()

    self.updateConfig()

  def setInputFields(self):
    self.selfNameInput.setText(self.config.members.selfName)
    for i, memberWidget in enumerate(self.memberWidgetGroup.memberWidgets):
      memberWidget.nameInput.setText(self.config.members.memberNames[i])

  def addMember(self):
    self.config.members.memberNames.append('')
    self.memberWidgetGroup.addName()
