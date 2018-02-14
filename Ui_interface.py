# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from random import *
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1300, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home_button = QtWidgets.QPushButton(Form)
        self.home_button.setIcon(QtGui.QIcon("icon/home.png"))
        self.home_button.setObjectName("home_button")
        self.horizontalLayout.addWidget(self.home_button)
        self.file_button = QtWidgets.QPushButton(Form)
        self.file_button.setIcon(QtGui.QIcon("icon/folder.png"))
        self.file_button.setObjectName("file_button")
        self.horizontalLayout.addWidget(self.file_button)
        self.camera_button = QtWidgets.QPushButton(Form)
        self.camera_button.setIcon(QtGui.QIcon("icon/Camera.png"))
        self.camera_button.setObjectName("camera_button")
        self.horizontalLayout.addWidget(self.camera_button)
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setIcon(QtGui.QIcon("icon/settings.png"))
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout.addWidget(self.settings_button)
        self.yolo_button = QtWidgets.QPushButton(Form)
        self.yolo_button.setText("yolo")
        self.yolo_button.setIcon(QtGui.QIcon("icon/yolo.png"))
        self.yolo_button.setObjectName("yolo_button")
        self.yolo_button.hide()
        self.horizontalLayout.addWidget(self.yolo_button)
        self.tiny_yolo_button = QtWidgets.QPushButton(Form)
        self.tiny_yolo_button.setText("tiny yolo")
        self.tiny_yolo_button.setIcon(QtGui.QIcon("icon/yolo.png"))
        self.tiny_yolo_button.hide()
        self.tiny_yolo_button.setObjectName("tiny_yolo_button")
        self.horizontalLayout.addWidget(self.tiny_yolo_button)
        self.about_us_button = QtWidgets.QPushButton(Form)
        self.about_us_button.setIcon(QtGui.QIcon("icon/info.png"))
        self.about_us_button.setObjectName("about_us_button")
        self.horizontalLayout.addWidget(self.about_us_button)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.french_button = QtWidgets.QPushButton(Form)
        self.french_button.setIcon(QtGui.QIcon("icon/france.ico"))
        self.french_button.setObjectName("french_button")
        self.horizontalLayout.addWidget(self.french_button)
        self.english_button = QtWidgets.QPushButton(Form)
        self.english_button.setIcon(QtGui.QIcon("icon/angleterre.ico"))
        self.english_button.setObjectName("english_button")
        self.horizontalLayout.addWidget(self.english_button)
        self.chinese_button = QtWidgets.QPushButton(Form)
        self.chinese_button.setIcon(QtGui.QIcon("icon/chine.ico"))
        self.chinese_button.setObjectName("chinese_button")
        self.horizontalLayout.addWidget(self.chinese_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setFont(font)
        self.image_label.setTextFormat(QtCore.Qt.AutoText)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout_2.addWidget(self.image_label)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.emoji_label = QtWidgets.QLabel(Form)
        self.emoji_label.setFont(font)
        self.emoji_label.setObjectName("emoji_label")
        self.horizontalLayout_2.addWidget(self.emoji_label)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_label = QtWidgets.QLabel(Form)
        self.left_label.setObjectName("left_label")
        self.horizontalLayout_3.addWidget(self.left_label)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setFixedSize(640, 480)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.convert_button = QtWidgets.QPushButton(Form)
        self.convert_button.setIcon(QtGui.QIcon("icon/convert.png"))
        self.convert_button.setIconSize(QtCore.QSize(40, 40))
        self.convert_button.setObjectName("convert_button")
        self.convert_button.setFont(font)
        self.horizontalLayout_4.addWidget(self.convert_button)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.scene = QtWidgets.QGraphicsScene()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.french_button.clicked.connect(self.setFrench)
        self.english_button.clicked.connect(self.setEnglish)
        self.chinese_button.clicked.connect(self.setChinese)
        self.settings_button.clicked.connect(self.settings)
        self.about_us_button.clicked.connect(self.show_about_us)

        self.scene = QtWidgets.QGraphicsScene()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "img2emoji"))
        self.image_label.setText(_translate("Form", "Image"))
        self.emoji_label.setText(_translate("Form", "Emojis"))
        self.chinese_button.setText(_translate("Form", "中文"))
        self.french_button.setText(_translate("Form", "Français"))
        self.english_button.setText(_translate("Form", "English"))
        self.setFrench()

    def update_left_label_with_file(self, fileName):
        self.left_label.setPixmap(QtGui.QPixmap(fileName).scaled(640, 480))

    def update_left_label_with_video(self, srcMat):
        height, width, bytesPerComponent= srcMat.shape
        bytesPerLine = bytesPerComponent* width
        srcQImage= QtGui.QImage(srcMat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        srcQPix=QtGui.QPixmap.fromImage(srcQImage)
        self.left_label.setPixmap(srcQPix)

    def show_home_image(self):
        self.left_label.setPixmap(QtGui.QPixmap("icon/home.jpg").scaled(640, 480))

    def update_right_home_scene(self):
        random_file = os.listdir('emojis/')[randint(1, 87)]
        lig = randint(1, 3)
        col = randint(1, 3)
        for file_name in [os.path.join('emojis', 'null.png'), os.path.join('emojis', random_file)]:
            item=QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(file_name).scaled(128,128))
            self.scene.addItem(item)
            item.setPos(col*128,lig*128)
        self.graphicsView.setScene(self.scene)

    def update_right_result_scene(self, results):
        scene = QtWidgets.QGraphicsScene()
        for i, result in enumerate(results):
            filename=os.path.join('emojis', result+'.png')
            item=QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(filename).scaled(128,128))
            scene.addItem(item)
            lig = i/3
            col = i%3
            item.setPos(col*128,lig*128)
        self.graphicsView.setScene(scene)

    def settings(self):
        if self.yolo_button.isVisible():
            self.yolo_button.hide()
            self.tiny_yolo_button.hide()
        else:
            self.yolo_button.show()
            self.tiny_yolo_button.show()

    def show_about_us(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle('Imamapi')
        msgBox.setIconPixmap(QtGui.QPixmap("icon/img.jpg").scaled(640, 640))
        ret = msgBox.exec_()


    def setFrench(self):
        self.home_button.setText("Accueil")
        self.file_button.setText("Ouvrir un fichier")
        self.convert_button.setText("Convertir!")
        self.camera_button.setText("Ouvrir la caméra")
        self.settings_button.setText("Paramètres")
        self.about_us_button.setText("À propos de nous")
    def setEnglish(self):
        self.home_button.setText("Home")
        self.file_button.setText("open file")
        self.convert_button.setText("Convert!")
        self.camera_button.setText("Open camera")
        self.settings_button.setText("Settings")
        self.about_us_button.setText("About us")
    def setChinese(self):
        self.home_button.setText("回到主页")
        self.file_button.setText("打开文件")
        self.convert_button.setText("转换！")
        self.camera_button.setText("打开摄像头")
        self.settings_button.setText("设置")
        self.about_us_button.setText("关于我们")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
