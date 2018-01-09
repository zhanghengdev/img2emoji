import Ui_interface
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import yolo_detection
import os, sys

class img2emoji():
    def __init__(self):
        self.Form=QtWidgets.QWidget()
        self.ui = Ui_interface.Ui_Form()
        self.ui.setupUi(self.Form)
        self.videoCapture=cv2.VideoCapture()
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.updateFrame)

        self.home_timer=QtCore.QTimer()
        self.home_timer.timeout.connect(self.ui.update_right_home_scene)
        self.home_timer.start(1000/5)

        self.ui.file_button.clicked.connect(self.openImage)
        self.ui.camera_button.clicked.connect(self.captureImage)
        self.ui.convert_button.clicked.connect(self.detection)
        self.ui.yolo_button.clicked.connect(self.load_yolo)
        self.ui.tiny_yolo_button.clicked.connect(self.load_tiny_yolo)
        self.net, self.meta=yolo_detection.load_detector()
        self.mode = 'image'

    def free_network(self):
        try:
            yolo_detection.free_net(self.net)
        except:
            print('Can not free network')
            pass
    def load_yolo(self):
        yolo_detection.free_net(self.net)
        self.net, self.meta=yolo_detection.load_detector()
    def load_tiny_yolo(self):
        yolo_detection.free_net(self.net)
        self.net, self.meta=yolo_detection.load_detector(cfg="cfg/tiny-yolo.cfg", weights="tiny-yolo.weights")

    def openImage(self):
        self.home_timer.stop()
        if self.mode == 'camera':
            self.videoCapture.release()
            self.timer.stop()
        self.mode = 'image'
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self.Form,  "choose a file",  "",  "Image Files (*.png *.bmp *.jpg *.tif *.GIF)")
        self.ui.update_left_label_with_file(fileName)

    def captureImage(self):
        self.home_timer.stop()
        if self.mode == 'image':
            self.mode = 'camera'
            if self.videoCapture.open(0):
                self.timer.start(1000/25)
            else:
                print("camera configuration failed")

    def updateFrame(self, file=False):
        ret, srcMat=self.videoCapture.read()
        srcMat=cv2.resize(srcMat, (640, 480), interpolation=cv2.INTER_CUBIC)
        srcMat=cv2.flip(srcMat, 1)
        cv2.cvtColor(srcMat, cv2.COLOR_BGR2RGB,srcMat)
        self.ui.update_left_label_with_video(srcMat)

    def detection(self):
        img_detc=self.ui.left_label.pixmap()
        try:
            img_detc.save("temp.jpg")
            results = yolo_detection.detec_img_with_preloaded_detector("temp.jpg", self.net, self.meta)
            self.ui.update_right_result_scene(results)
            print(results)
            os.system('rm temp.jpg')
        except:
            print("detection failed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaceFun=img2emoji()
    interfaceFun.Form.show()
    sys.exit(app.exec_())
