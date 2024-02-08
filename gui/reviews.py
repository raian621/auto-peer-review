from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from docgen import generate_peer_review_doc


class ReviewsWidget(QWidget):
  reviews = dict()

  def __init__(self, parent=None, setView=None):
    QWidget.__init__(self, parent)
    if setView != None:
      self.setView = setView
    self.setContentsMargins(0, 0, 0, 0)
    QLabel("Reviews", self)
    backButton = QPushButton(self)
    backButton.setText("Back to menu")
    backButton.clicked.connect(lambda: self.setView('main'))

  def addReview(self, name: str, review: dict()):
    self.reviews[name] = review

  def saveReviews(self, filepath):
    generate_peer_review_doc(self.reviews, filepath)

  def setMembers(self, members):
    self.members = members
