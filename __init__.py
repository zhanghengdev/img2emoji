import Ui_interface
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import yolo_detection 
class InterFaceFunctions():
    def __init__(self):
        self.Form=QtWidgets.QWidget()
        self.ui = Ui_interface.Ui_Form()
        self.ui.setupUi(self.Form)
        self.videoCapture=cv2.VideoCapture()
        self.timer=QtCore.QTimer()
        self.ui.pushButton.clicked.connect(self.openImage)
        self.ui.pushButton_2.clicked.connect(self.captureImage)
        self.ui.pushButton_3.clicked.connect(self.detection)
	
	self.ui.pushButton.setIconSize(QtCore.QSize(40,40))
	self.ui.pushButton.setIcon(QtGui.QIcon("./folder.png"))
	self.ui.pushButton.setFlat(True)
	self.ui.pushButton.setText("")

	self.ui.pushButton_2.setIconSize(QtCore.QSize(40,40))
	self.ui.pushButton_2.setIcon(QtGui.QIcon("./Camera.png"))
	self.ui.pushButton_2.setFlat(True)
	self.ui.pushButton_2.setText("")

        self.ui.pushButton_3.setText("detecter")
	self.net,self.meta=yolo_detection.load_detector()

	
        
    def openImage(self):
        fileName1, filetype = QtWidgets.QFileDialog.getOpenFileName(self.Form,  "choose a file",  "",  "Image Files (*.png *.bmp *.jpg *.tif *.GIF)")
        self.ui.label_4.setPixmap(QtGui.QPixmap(fileName1)) 
        self.flag=0
        
        
    def captureImage(self):
        if self.videoCapture.open(0):
            self.timer.timeout.connect(self.updateFrame)
            self.timer.start(1000/20)
            self.ui.pushButton_3.setText("capturer")
        else:
            print("camera configuration failed")
        
    def updateFrame(self):
        ret, srcMat=self.videoCapture.read()
        srcMat=cv2.resize(srcMat, (320, 240), interpolation=cv2.INTER_CUBIC)
        srcMat=cv2.flip(srcMat, 1)
        cv2.cvtColor(srcMat, cv2.COLOR_BGR2RGB,srcMat)
        height, width, bytesPerComponent= srcMat.shape
        bytesPerLine = bytesPerComponent* width
        srcQImage= QtGui.QImage(srcMat.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        srcQPix=QtGui.QPixmap.fromImage(srcQImage)
        self.ui.label_4.setPixmap(srcQPix)
        
    def detection(self):
        if self.ui.pushButton_3.text()=="capturer":
            self.ui.pushButton_3.setText("detecter")
            self.videoCapture.release()
            self.timer.stop()
        else:
            img_detc=self.ui.label_4.pixmap()
            if (img_detc.save("temp.jpg")):
                print("save completed")
		results=yolo_detection.detec_img_with_preloaded_detector("temp.jpg",self.net,self.meta)
		scene=QtWidgets.QGraphicsScene()
		i=0
		print(results)
		for result in results:
			i=i+1
			filename='./emojis/{}'.format(result)
			
			item=QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(filename).scaled(256,256))
			item.setScale(0.5)
			scene.addItem(item)
			lig=(int(i)-1)/2
			col=(int(i)-1)%2
			item.setPos(col*129,lig*129)
		self.ui.graphicsView.setScene(scene)
			
		
            else:
                print("failed save")
                
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaceFun=InterFaceFunctions()
    interfaceFun.Form.show()
    sys.exit(app.exec_())
