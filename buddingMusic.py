from PyQt5.QtCore import QUrl 
from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimedia import QMediaPlaylist
from PyQt5.QtMultimedia import QMediaContent
import os

# need to modify in buddingMainWindow.py:
#self.voiceButton = buddingMusic.BuddingVoice(self.tailWidget, self.controller)

class BuddingVoice(QtWidgets.QPushButton):
    def __init__(self, parent, controller):
        super(BuddingVoice, self).__init__(parent)
        # music button config.
        self.controller = controller
        self.controller.register_observer("music_button", self)
        self.clicked.connect(self.voice_clicked)
        self.musicon = 1

        #playlist, set according to level
        self.playlist = QMediaPlaylist()
        self.url = None
        self.level = self.controller.get_level()
        print("user level", self.level)
        #below is for test
        #self.level = 3
        self.url = self.choose_music(self.level)
        self.playlist.addMedia(QMediaContent(self.url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        
        #player
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()

    def voice_clicked(self):
        if self.musicon:
            self.player.pause()
        else:
            #below is for test on_level_update
            #self.on_level_update()
            self.player.play()
        self.musicon = 1 - self.musicon

    def on_level_update(self, newlevel):
        #below is for test
        #newlevel = self.level + 1
        print("newlevel", newlevel, "oldlevel", self.level)
        self.player.pause()
        self.playlist.removeMedia(0)
        self.url = self.choose_music(newlevel)
        self.playlist.addMedia(QMediaContent(self.url))
        self.player.setPlaylist(self.playlist)
        self.player.play()
        self.level = newlevel

    def music_path(self, music):
        fp = "./music/" + music
        return os.path.abspath(fp)

    def choose_music(self, level):
        mystr = ""
        if level == 1:
            mystr = self.music_path("sad.mp3")
        elif level == 2:
            mystr = self.music_path("neutral.mp3")
        else:
            mystr = self.music_path("happy.mp3")
        return QUrl.fromLocalFile(mystr)

    def on_logout(self):
        self.musicon = 0
        self.player.stop()