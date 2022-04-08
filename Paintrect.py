import sys
from PIL import ImageQt, Image
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from FileTest import Ui_MainWindow
import numpy as np
import cv2
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 设置当前不可作图
        self.flagPaint = False
        # connect the slot when you push the button putton：clicked.connect
        self.actionNew.triggered.connect(self.getImage)
        self.actionNew1.triggered.connect(self.saveImage)


    def getImage(self):
        # 该方法会启动文件对话框，当你选择某文件后，返回文件绝对路径和文件类型
        fdir, ftype = QFileDialog.getOpenFileName(self,
                                                  "Select Image",
                                                  "./",
                                                  "Image Files (*.png *.jpg)")
        # 把选择的图片展示在label上
        # img = Image.open(fdir)
        # img = self.transImg(img)
        # self.label.setPixmap(img)
        # 载入图片
        Qimage = QImage()
        Qimage.load(fdir)
        # # 旋转变换
        # transform = QTransform()
        # transform.rotate(-90) #逆时针旋转90
        # # 应用到image
        # Qimage = Qimage.transformed(transform)
        # 创建QPixmap
        img_path_code = np.fromfile(fdir, dtype=np.uint8)  # 含有中文路径时
        img = cv2.imdecode(img_path_code, 0)
        self.label.rawPic = img
        self.label.wRadio,self.label.hRadio = img.shape[1]/452,img.shape[0]/827
        pic_image = QPixmap.fromImage(Qimage).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pic_image)

        # 初始化画布，允许作图
        self.label.initDrawing(pic_image)
        self.label.drawingPermission(True)

        self.flagPaint = True

    def saveImage(self):
        if self.flagPaint:
            img = self.label.pix.toImage()
            # 该方法同上
            fdir, ftype = QFileDialog.getSaveFileName(self, "Save Image",
                                                      "./", "Image Files (*.jpg)")
            img.save(fdir)

    def transImg(self, img):
        '''
        use to trans PIL img to Qt img
        :param img: PIL object
        :return: Qt object
        '''
        img = img.resize((self.label.width(), self.label.height()))
        return ImageQt.toqpixmap(img)

if __name__ == "__main__":
    # 此句解决Qt Designer和Pycharm显示不同的问题
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
