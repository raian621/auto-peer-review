from PyQt6.QtWidgets import *
from docgen import generate_peer_review_doc
from data import DOCX_TEMPLATE_PATH


class SaveDocWindow(QWidget):
  def __init__(self, reviews, parent=None):
    QWidget.__init__(self, parent)
    self.setWindowTitle('Save generated document to file')
    self.reviews = reviews
    self.filename = ''
    self.resize(200, 200)

    layout = QVBoxLayout()
    self.setLayout(layout)
    fileChooserLayout = QHBoxLayout()
    layout.addWidget(QLabel('Output file path:'))
    layout.addLayout(fileChooserLayout)

    self.filenameInput = QLineEdit()
    self.filenameInput.textChanged[str].connect(self.setFilename)
    fileChooserLayout.addWidget(self.filenameInput)
    self.browseButton = QPushButton('Browse')
    self.browseButton.clicked.connect(self.browseFiles)
    fileChooserLayout.addWidget(self.browseButton)
    self.saveButton = QPushButton('Save')
    self.saveButton.clicked.connect(self.saveDocument)
    layout.addWidget(self.saveButton)

  def setFilename(self, filename):
    userTyping = False
    userCursorPos = 0

    if self.filename == filename:
      # if we set the text of filenameInput programmatically this function could
      # infinitely recurse. this stops the infinite recursion:
      return
    elif filename == self.filenameInput.text():
      userTyping = True
      userCursorPos = self.filenameInput.cursorPosition()

    self.filename = filename
    self.filenameInput.setText(filename)
    self.saveButton.setEnabled(filename != '')

    if userTyping:
      self.filenameInput.setCursorPosition(userCursorPos)

  def browseFiles(self):
    self.setFilename(QFileDialog.getSaveFileName()[0])

  def saveDocument(self):
    generate_peer_review_doc(
      self.reviews,
      self.filename,
      DOCX_TEMPLATE_PATH
    )
    self.close()
