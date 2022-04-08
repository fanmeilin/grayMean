# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPen,QFont
from PyQt5.QtCore import Qt, QPoint
import numpy as np

class MyLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.drawable = False
        self.wRadio,self.hRadio = 1,1

    # 是否允许作图
    def drawingPermission(self, a):
        if isinstance(a, bool):
            self.drawable = a

    # 初始化画布
    def initDrawing(self, img):
        self.pix = img  # 当前图
        self.tmpPix = self.pix.copy()  # 上一张图
        self.lastPoint = QPoint()
        self.endPoint = QPoint()

    def paintEvent(self, event):
        # 先执行父类方法，必须加上
        # super().paintEvent(event)

        if self.drawable:
            pp = QPainter(self)
            pp.begin(self)
            pp.drawPixmap(0, 0, self.pix)
            pp.end()

    def mousePressEvent(self, event):
        # 先执行父类方法，可不加
        super().mousePressEvent(event)
        if self.drawable:
            # 鼠标左键按下
            if event.button() == Qt.LeftButton:
                self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        # 先执行父类方法，可不加
        super().mouseMoveEvent(event)
        if self.drawable:
            # 鼠标左键按下的同时移动鼠标
            if event.buttons() and Qt.LeftButton:
                self.endPoint = event.pos()

                # 当前图复制上一张图
                self.pix = self.tmpPix.copy()

                pp = QPainter(self.pix)
                pp.setPen(QPen(Qt.green, 2))
                pp.drawRect(self.lastPoint.x(), self.lastPoint.y(),
                            self.endPoint.x() - self.lastPoint.x(),
                            self.endPoint.y() - self.lastPoint.y())
                #显示数值
                # pp = QPainter(self.pix)
                # pp.begin(self.pix)
                picx,picy,picw,pich = self.lastPoint.x()*self.wRadio, self.lastPoint.y()*self.hRadio,(self.endPoint.x() - self.lastPoint.x())*self.wRadio,(self.endPoint.y() - self.lastPoint.y())*self.hRadio
                y1,y2,x1,x2 = min(int(picy),int(picy+pich)),max(int(picy),int(picy+pich)),min(int(picx),int(picx+picw)),max(int(picx),int(picx+picw))
                crop_img = self.rawPic[y1:y2,x1:x2]
                avg_local = round(np.mean(crop_img), 3)
                # pp.setPen(QPen(Qt.green, 3))
                pp.setFont(QFont('Times New Roman', 13))
                pp.drawText(self.lastPoint.x()+10, self.lastPoint.y()+15,str(avg_local))
                # pp.end()
                # 更新label
                self.update()

    def mouseReleaseEvent(self, event):
        # 先执行父类方法，可不加
        super().mouseReleaseEvent(event)
        if self.drawable:
            # 鼠标左键释放
            if event.button() == Qt.LeftButton:
                # 上一张图指向当前图
                self.tmpPix = self.pix

