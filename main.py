import time
from window import Ui_MainWindow

from PySide2.QtCore import * 
from PySide2.QtGui import *  
from PySide2.QtWidgets import *  

import os, sys
import yt_dlp as youtube_dl

#create our main class
class Logic(QMainWindow):
    def __init__(self):
        super(Logic, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #set variables
        self.download = False
        self.folder = None
        self.yt_options = {
                'format': 'bestaudio/best',
                'postprocessors': [
                {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                }
            ]
        }

        #our methods
        self.connect()
        self.lock()
        self.show()

    #methods we use for mainwindow
    def connect(self):
        self.ui.pushButton.clicked.connect(self.choose_folder)
        self.ui.pushButton_2.clicked.connect(self.download_video)

    def lock(self):
        if self.download:
            print("yes")
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)

    #methods we use for download video
    def choose_folder(self):
        try:
            self.folder = QFileDialog.getExistingDirectory(self, "Choose folder to save mp3")
            self.ui.plainTextEdit.setPlainText("")
            self.ui.pushButton.setText(self.folder)
            os.chdir(self.folder)
            self.ui.plainTextEdit.setPlainText("")
        except FileNotFoundError:
            self.ui.plainTextEdit.setPlainText("Please choose a folder!")

    def download_video(self):
        try:
            url = self.ui.lineEdit.text()

            self.ui.plainTextEdit.setPlainText("downloading...")
            #download at start a video
            if self.folder is not None:
                with youtube_dl.YoutubeDL(self.yt_options) as ydl:
                    self.download = True
                    ydl.download([url])
            else:
                self.ui.plainTextEdit.setPlainText("Please choose a folder!")
            
            self.ui.plainTextEdit.setPlainText("finised!!!!!!!!")
            self.download = False
        except Exception as e:
            self.ui.plainTextEdit.setPlainText(e)
            self.ui.plainTextEdit.setPlainText("Please enter a correct url to download!")

if __name__ == '__main__':
    app = QApplication()
    log = Logic()
    sys.exit(app.exec_())
