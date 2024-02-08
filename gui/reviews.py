from PyQt6.QtWidgets import QWidget, QLabel
from docgen import generate_peer_review_doc

class ReviewsWidget(QWidget):
    reviews = dict()
    
    def __init__(self, parent=None, setView=None):
        QWidget.__init__(self, parent)
        if setView != None:
            self.setView = setView
        QLabel("Reviews", self)
        
    def addReview(self, name: str, review: dict()):
        self.reviews[name] = review
        
    def saveReviews(self, filepath):
        generate_peer_review_doc(self.reviews, filepath)