from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from .save_doc_window import SaveDocWindow


REVIEW_STAR_DESCRIPTIONS = {
  'quality': 'Quality of work',
  'quantity': 'Quantity of work',
  'initiative': 'Initiative, creativity, experience, leadership',
  'dependability': 'Dependability and meeting commitments',
  'interaction':
    'Interaction, supporting other team members, sharing information',
  'meetings': 'Team meetings -- Participation, punctuality',
  'overall': 'Overall contributions'
}


class StarsWidget(QWidget):
  def __init__(self, stars, updateReview, parent=None):
    QWidget.__init__(self, parent)
    self.stars = stars
    self.updateReview = updateReview

    layout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(5)

    self.starButtons = [QPushButton(f'{i + 1}') for i in range(5)]
    for i in range(len(self.starButtons)):
      self.starButtons[i].clicked.connect(
        lambda _, stars=i + 1: self.setStars(stars)
      )
      layout.addWidget(self.starButtons[i])

    self.setLayout(layout)

  def setStars(self, stars):
    self.stars = stars
    for i in range(0, stars):
      self.starButtons[i].setStyleSheet('background-color: yellow')
    for i in range(stars, 5):
      self.starButtons[i].setStyleSheet(None)
    self.updateReview()

  def getStars(self):
    return self.stars


class ReviewsWidget(QWidget):
  reviews = dict()

  def __init__(self, setView, memberNames, parent=None):
    QWidget.__init__(self, parent)
    self.setView = setView
    self.memberNames = memberNames
    self.reviewIndex = 0

    self.initReviews()
    self.setUpUI()

  def setUpUI(self):
    layout = QVBoxLayout()
    layout.setContentsMargins(10, 10, 10, 10)
    self.setLayout(layout)
    header = QHBoxLayout()
    header.setAlignment(Qt.AlignmentFlag.AlignTop)
    layout.addLayout(header)
    body = QVBoxLayout()
    layout.addLayout(body)
    footer = QHBoxLayout()
    footer.setAlignment(Qt.AlignmentFlag.AlignBottom)
    layout.addLayout(footer)

    titleLabel = QLabel('Reviews')
    titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    header.addWidget(titleLabel)

    nameLabel = QLabel(self.memberNames[0])
    self.nameLabel = nameLabel

    self.starInputs = dict()
    body.addWidget(nameLabel)
    for key in REVIEW_STAR_DESCRIPTIONS.keys():
      starDescription = QLabel(REVIEW_STAR_DESCRIPTIONS[key])
      starDescription.setWordWrap(True)
      body.addWidget(starDescription)
      self.starInputs[key] = StarsWidget(0, self.tryUnlockForwardButton)
      body.addWidget(self.starInputs[key])

    body.addWidget(QLabel(
      'Comments/feedback -- detailed, specific comments are needed here to '
      'earn full credit.'
    ))
    self.commentInput = QTextEdit()
    self.commentInput.textChanged.connect(
      self.tryUnlockForwardButton
    )
    body.addWidget(self.commentInput)

    backButton = QPushButton()
    self.backButton = backButton
    backButton.setText('Back to menu')
    backButton.clicked.connect(self.goBack)
    footer.addWidget(backButton)
    forwardButton = QPushButton()
    self.forwardButton = forwardButton
    self.forwardButton.setEnabled(False)
    forwardButton.setText('Next')
    forwardButton.clicked.connect(self.goForward)
    footer.addWidget(forwardButton)

  def initReviews(self):
    self.reviews = [{
      'name': name,
      'quality': 0,
      'quantity': 0,
      'initiative': 0,
      'dependability': 0,
      'interaction': 0,
      'meetings': 0,
      'overall': 0,
      'comments': ''
    } for name in self.memberNames]

  def tryUnlockForwardButton(self):
    shouldUnlock = True
    for key in REVIEW_STAR_DESCRIPTIONS.keys():
      if self.starInputs[key].getStars() == 0:
        shouldUnlock = False
    if len(self.commentInput.toPlainText()) == 0:
      shouldUnlock = False

    self.forwardButton.setEnabled(shouldUnlock)

  def saveReviews(self):
    self.saveDocWindow = SaveDocWindow(self.reviews, None)
    self.saveDocWindow.show()
    self.setView('main')

  def showCurrentReview(self):
    self.nameLabel.setText(self.memberNames[self.reviewIndex])
    for key in self.starInputs.keys():
      self.starInputs[key].setStars(self.reviews[self.reviewIndex][key])
    self.commentInput.setText(self.reviews[self.reviewIndex]['comments'])
    self.tryUnlockForwardButton()

  def updateCurrentReview(self):
    for key in self.starInputs.keys():
      self.reviews[self.reviewIndex][key] = self.starInputs[key].getStars()
    self.reviews[self.reviewIndex]['comments'] = self.commentInput.toPlainText()

  def setMembers(self, memberNames):
    self.memberNames = memberNames

  def goBack(self):
    self.updateCurrentReview()
    if self.reviewIndex == 0:
      self.setView('main')
      return
    elif self.reviewIndex == 1:
      self.backButton.setText('Back to menu')
    else:
      self.forwardButton.setText('Next')
    self.reviewIndex -= 1
    self.showCurrentReview()

  def goForward(self):
    self.updateCurrentReview()
    if self.reviewIndex == len(self.reviews) - 1:
      self.saveReviews()
      return
    elif self.reviewIndex == len(self.reviews) - 2:
      self.forwardButton.setText('Generate document')
    else:
      self.backButton.setText('Previous')
    self.reviewIndex += 1
    self.showCurrentReview()
