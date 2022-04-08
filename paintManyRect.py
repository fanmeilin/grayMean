from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

__appname__ = 'painter'
class Rect:

    def __init__(self):
        self.start = QPoint()
        self.end = QPoint()

    def setStart(self, s):
        self.start = s

    def setEnd(self, e):
        self.end = e

    def startPoint(self):
        return self.start

    def endPoint(self):
        return self.end

    def paint(self, painter):
        painter.drawRect(self.startPoint().x(), self.startPoint().y(), self.endPoint().x() - self.startPoint().x(),
                         self.endPoint().y() - self.startPoint().y())


class PaintCanvas(QWidget):

    def __init__(self, *args, **kwargs):
        super(PaintCanvas, self).__init__(*args, **kwargs)  # 继承父类
        self.setMouseTracking(True)  # 保证得到鼠标信息
        self.drawingRectColor = QColor(0, 255, 0)
        self.rectList = []  # 矩形对象列表
        self.perm = False  # 描述在不在画
        self.shape = None  # 储存画的矩形对象
        self.painter = QPainter(self)


    def mouseMoveEvent(self, ev):
        pos = ev.pos()  # 得到鼠标位置
        window = self.parent().window()  # 得到窗口对象
        if window is not None:
            self.parent().window().labelCoordinates.setText('X: %d; Y: %d' % (pos.x(), pos.y()))  # 设置窗口状态栏信息
        if ev.buttons() & Qt.LeftButton:
            if self.shape is not None and not self.perm:
                self.shape.setEnd(ev.pos())
                self.update()


    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.shape = Rect()
            if (self.shape is not None):
                self.perm = False
                self.rectList.append(self.shape)
                self.shape.setStart(ev.pos())
                self.shape.setEnd(ev.pos())
            self.update()


    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.perm = True
            self.shape = None
            self.update()

    def paintEvent(self, ev):
        p = self.painter
        p.begin(self)
        p.setPen(self.drawingRectColor)
        brush = QBrush(Qt.BDiagPattern)
        p.setBrush(brush)
        for shape in self.rectList:
            shape.paint(p)
        p.end()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle(__appname__)
        self.paintCanvas = PaintCanvas(parent=self)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.paintCanvas)
        self.scroll.setWidgetResizable(True)
        self.setCentralWidget(self.scroll)
        self.statusBar().showMessage('%s started.' % __appname__)
        self.statusBar().show()
        self.labelCoordinates = QLabel('')
        self.statusBar().addPermanentWidget(self.labelCoordinates)

def get_main_app(argv=[]):
    app = QApplication(argv)
    app.setApplicationName(__appname__)
    win = MainWindow()
    win.show()
    return app, win


app, _win = get_main_app(sys.argv)
sys.exit(app.exec_())



