import os

import cv2
import requests
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread


class EmotionThread(QThread):
    TEMP_FILENAME = "capture.jpeg"
    sig = pyqtSignal(list)

    def __init__(self):
        QThread.__init__(self)
        self.msg = None

    def __del__(self):
        self.wait()

    def run(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        subscription_key = "9c2a662ceba54c96902f6b78430f01bb"

        emotion_recognition_url = "https://eastus.api.cognitive.\
                    microsoft.com/face/v1.0/detect"

        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion',
        }
        cap.release()
        cv2.imwrite(self.TEMP_FILENAME, frame)
        with open(self.TEMP_FILENAME, 'rb') as f:
            image_data = f.read()

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            "Content-Type": "application/octet-stream",
        }
        response = requests.post(
            emotion_recognition_url, headers=headers,
            params=params, data=image_data,
        )
        response.raise_for_status()
        analysis = response.json()
        os.remove(self.TEMP_FILENAME)
        self.sig.emit(analysis)


class BuddingEmotion:
    def __init__(self, controller):
        print("init")
        self.controller = controller

    def startRecog(self):
        print("start recog")
        self.emotionThread = EmotionThread()
        self.emotionThread.sig.connect(self.processResult)
        self.emotionThread.start()

    def processResult(self, message):
        try:
            print(message)
            ratio = float(message[0]['faceAttributes']['emotion']['happiness'])
            if ratio > 0.1:
                self.controller.onSuccessEvent()
            else:
                self.controller.onFailEvent()
        except Exception as e:
            print("error occur, fail, Exception: ", e)

    # user click button again
    def stopRecog(self):
        print("stop recog")
        if self.emotionThread.isFinished() is False:
            print("kill the current thread")
            self.emotionThread.terminate()
            self.emotionThread.wait()
