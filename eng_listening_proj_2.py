"""
Business view
I have 10 words with the youtube links
I start the app
I hear the sequence of 10 x 10 sec audio for those 10 words
After that it stops playing. I enjoy the process and better know those 10 words
Then, I repeat this process with the other 10, 20, 50 words, with some repetition cycle and train myself
  to know it better and better
"""

__version__ = 'v1.1'
__author__ = 'Iurii'

import os
import sys
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtCore import QRect, QUrl, QCoreApplication, QMetaObject, QTimer
from PyQt5.QtCore import Qt, QUrl, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWidgets import QApplication

words = [
    ["poverty", "https://www.youtube.com/embed/15-DE4i30m8?autoplay=1&mute=0&start=202&end=212;rel=0"],
    ["promenade", "https://www.youtube.com/embed/qM0uOAqrVb0?autoplay=1&mute=0&start=653&end=663;rel=0"],
    ["sameness", "https://www.youtube.com/embed/o1Z4F4e2Bw4?autoplay=1&mute=0&start=589&end=599;rel=0"],
    ["allay", "https://www.youtube.com/embed/a0KtqDTmDa4?autoplay=1&mute=0&start=2731&end=2741;rel=0"],
    ["ramble", "https://www.youtube.com/embed/xveWHTbZ2_o?autoplay=1&mute=0&start=238&end=248;rel=0"],
    ["vivacity", "https://www.youtube.com/embed/aV-5NXwo19o?autoplay=1&mute=0&start=804&end=814;rel=0"],
    ["greed", "https://www.youtube.com/embed/qZjr2CIEflc?autoplay=1&mute=0&start=340&end=350;rel=0"],
    ["stroll", "https://www.youtube.com/embed/7xeFP0SEDdc?autoplay=1&mute=0&start=2414&end=2424;rel=0"],
    ["exacerbate", "https://www.youtube.com/embed/15-DE4i30m8?autoplay=1&mute=0&start=445&end=455;rel=0"],
    ["prosperity", "https://www.youtube.com/embed/87AEeLpodnE?autoplay=1&mute=0&start=759&end=769;rel=0"]
]

class YouTubePlayer(QWidget):
    def __init__(self):
        super().__init__()

        defaultSettings = QWebEngineSettings.globalSettings()
        defaultSettings.setFontSize(QWebEngineSettings.MinimumFontSize, 28)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        topLayout = QHBoxLayout()
        self.layout.addLayout(topLayout)

        label = QLabel('Enter Video Id: ')
        self.input = QLineEdit()
        self.input.installEventFilter(self)
        self.input.setText("test test")

        topLayout.addWidget(label, 1)
        topLayout.addWidget(self.input, 9)

        self.webview = self.addWebView()

        buttonLayout = QHBoxLayout()
        self.layout.addLayout(buttonLayout)

        
        self.word_num = 1
        self._updator = QTimer(self)
        self._updator.setSingleShot(False)
        self._updator.timeout.connect(self.reload_next)

        self._updator.start(8000)
        

    def reload_next(self):
        self.word_num += 1
        if self.word_num >= len(words):
            self._updator.stop()

        self.webview.load(QUrl(words[self.word_num][1]))
        self.webview.show()

    def addWebView(self):
        self.webview = QWebEngineView()
        self.profile = QWebEngineProfile("my_profile", self.webview)
        self.profile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        self.webpage = QWebEnginePage(self.profile, self.webview)
        self.webpage.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)

        self.webview.setPage(self.webpage)
        self.webview.load(QUrl(words[0][1]))
        self.layout.addWidget(self.webview)
        return self.webview


class YouTubeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Player")
        self.setMinimumSize(800, 400)
        self.players = []

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        buttonAddPlayer = QPushButton('&Add Player')
        self.layout.addWidget(buttonAddPlayer)

        self.videoGrid = QGridLayout()
        self.layout.addLayout(self.videoGrid)

        self.player = YouTubePlayer()
        self.videoGrid.addWidget(self.player, 0, 0)

        self.layout.addWidget(QLabel(__version__ + ' by ' + __author__), alignment=Qt.AlignBottom | Qt.AlignRight)

        self.setStyleSheet("""
            QPushButton {
                font-size: 28px;
                height: 40px;
                background-color: #E41937;
                color: white;
            }

            * {
                background-color: #83C2FF;
                font-size: 30 px;
            }

            QLineEdit {
                background-color: white;
                color: black;
            }    
        """)

if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #NewMainWindow = YouTubePlayer()

    app = QApplication(sys.argv)

    window = YouTubeWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Player Window Closed')

    sys.exit(app.exec_())










