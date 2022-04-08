import cv2
import numpy as np
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

fname=''
one=0
two=0
three=180

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(900,500)
        self.center()   #使窗口居中
        self.setWindowTitle("label显示图片")
        self.setWindowIcon(QIcon('1.jpg'))

        self.label = QLabel(self)
        self.label.setText("   显示图片")
        self.label.setFixedSize(300, 400)
        self.label.move(200,30)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                 )

        self.label2 = QLabel(self)
        self.label2.setText("   显示图片")
        self.label2.setFixedSize(300, 400)
        self.label2.move(550, 30)

        self.label2.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                 )

        btn_1 = QPushButton(self)
        btn_1.setText("打开图片")
        btn_1.move(30, 30)
        btn_1.clicked.connect(self.openimage)

        btn_2 = QPushButton(self)
        btn_2.setText("图像旋转180")
        btn_2.move(30, 80)
        btn_2.clicked.connect(self.xaunzhuan180)

        btn_3 = QPushButton(self)
        btn_3.setText("图像向右平移")
        btn_3.move(30, 130)
        btn_3.clicked.connect(self.youyi)

        btn_4 = QPushButton(self)
        btn_4.setText("图像向下平移")
        btn_4.move(30, 180)
        btn_4.clicked.connect(self.xiayi)

        btn_5 = QPushButton(self)
        btn_5.setText("图像二值化")
        btn_5.move(30, 230)
        btn_5.clicked.connect(self.erzhihua)

        btn_6 = QPushButton(self)
        btn_6.setText("图像灰度")
        btn_6.move(30, 280)
        btn_6.clicked.connect(self.huidu)

        btn_7 = QPushButton(self)
        btn_7.setText("图像边缘检测")
        btn_7.move(30, 330)
        btn_7.clicked.connect(self.bianyuan)

        btn_8 = QPushButton(self)
        btn_8.setText("退出")
        btn_8.move(30, 380)
        btn_8.clicked.connect(QCoreApplication.quit)
        print("成功退出")

        btn_1 = QPushButton(self)
        btn_1.setText("清除图片")
        btn_1.move(30, 430)
        btn_1.clicked.connect(self.qingchu)

    def openimage(self):
        global fname
        global one
        global two
        QMessageBox.question(self, '提醒', '选择图片时要是绝对路径(且全英文路径)',
                                     QMessageBox.Ok )
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*;;*.png;;All Files(*)")
        # jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        # self.label.setPixmap(QPixmap(jpg))
        # self.label2.setPixmap(QPixmap(jpg))

        image=cv2.imread(imgName)
        if image is None:
            print("未选择图片")
        else:
            size = (int(self.label2.width()), int(self.label2.height()))
            shrink = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            fname = imgName
            print(imgName)
            one = 50
            two = 50

    def xaunzhuan180(self):
        global fname
        global three
        image=cv2.imread(fname)
        if image is None:
            print("未选择图片")
        else:
                h, w = image.shape[:2]
                M = cv2.getRotationMatrix2D((w / 2, h / 2), three, 1)   #旋转  通过getRotationMatrix2D得到图像旋转后的矩阵
                dst = cv2.warpAffine(image, M, (w, h))    #通过仿射变换函数warpAffine将矩阵转化为图像
                size = (int(self.label2.width()), int(self.label2.height()))    #获得控件lable的尺寸
                shrink = cv2.resize(dst, size, interpolation=cv2.INTER_AREA)   #对图像进行缩放
                shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
                self.QtImg = QtGui.QImage(shrink.data,
                                          shrink.shape[1],
                                          shrink.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                three+=180


    def youyi(self):
        global fname
        global one
        global two
        two=50
        image = cv2.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            if one==50:
                M = np.array([[1, 0, one], [0, 1, 0]], dtype=np.float32)
                image1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
                size = (int(self.label2.width()), int(self.label2.height()))
                shrink = cv2.resize(image1, size, interpolation=cv2.INTER_AREA)
                shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
                self.QtImg = QtGui.QImage(shrink.data,
                                          shrink.shape[1],
                                          shrink.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                one+=50
            else:
                M = np.array([[1, 0, one], [0, 1, 0]], dtype=np.float32)
                image1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
                size = (int(self.label2.width()), int(self.label2.height()))
                shrink = cv2.resize(image1, size, interpolation=cv2.INTER_AREA)
                shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
                self.QtImg = QtGui.QImage(shrink.data,
                                          shrink.shape[1],
                                          shrink.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                one += 50


    def xiayi(self):
        global fname
        global one
        global two
        one=50
        image = cv2.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            if two == 50:
                M = np.array([[1, 0, 0], [0, 1, two]], dtype=np.float32)
                image1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
                size = (int(self.label2.width()), int(self.label2.height()))
                shrink = cv2.resize(image1, size, interpolation=cv2.INTER_AREA)
                shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
                self.QtImg = QtGui.QImage(shrink.data,
                                          shrink.shape[1],
                                          shrink.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                two += 50
            else:
                M = np.array([[1, 0, 0], [0, 1, two]], dtype=np.float32)
                image1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
                size = (int(self.label2.width()), int(self.label2.height()))
                shrink = cv2.resize(image1, size, interpolation=cv2.INTER_AREA)
                shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
                self.QtImg = QtGui.QImage(shrink.data,
                                          shrink.shape[1],
                                          shrink.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                two += 50

    def erzhihua(self):
        global fname
        image = cv2.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            ret,binary=cv2.threshold(image,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY)
            print("二值化的阈值为:",ret)
            size = (int(self.label2.width()), int(self.label2.height()))
            shrink = cv2.resize(binary, size, interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      QtGui.QImage.Format_RGB888)
            self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def huidu(self):
        global fname
        image = cv2.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            size = (int(self.label2.width()), int(self.label2.height()))
            shrink = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      QtGui.QImage.Format_RGB888)
            self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def bianyuan(self):
        global fname
        image = cv2.imread(fname)
        if image is None:
            print("未选择图片")
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image1=cv2.Canny(image,50,120)
            size = (int(self.label2.width()), int(self.label2.height()))
            shrink = cv2.resize(image1, size, interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      QtGui.QImage.Format_RGB888)
            self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))


    def qingchu(self):
        self.label.setPixmap(QPixmap(""))
        self.label2.setPixmap(QPixmap(""))


    def center(self):  # 控制窗口显示在屏幕中心的方法

        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())

