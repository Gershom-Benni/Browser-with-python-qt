# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # Import QUrl
from util import fetch_url  # Import the fetch_url function from utils.py

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python Web Browser')
        self.setGeometry(100, 100, 1024, 768)

        self.browser = QWebEngineView(self)
        self.address_bar = QLineEdit(self)
        self.load_button = QPushButton('Go', self)
        self.source_button = QPushButton('Show Source', self)  # Button to show raw HTML

        layout = QVBoxLayout()
        layout.addWidget(self.address_bar)
        layout.addWidget(self.load_button)
        layout.addWidget(self.source_button)
        layout.addWidget(self.browser)

        self.source_text_edit = QTextEdit(self)
        self.source_text_edit.setVisible(False)  # Hide source text edit by default

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_button.clicked.connect(self.load_page)
        self.address_bar.returnPressed.connect(self.load_page)
        self.source_button.clicked.connect(self.show_source)

    def load_page(self):
        url = self.address_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))  # Convert string URL to QUrl

    def show_source(self):
        url = self.address_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        html_content = fetch_url(url)
        if html_content:
            self.source_text_edit.setText(html_content)
            self.source_text_edit.setVisible(True)
            self.source_text_edit.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
