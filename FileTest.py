from PyQt5 import QtCore, QtGui, QtWidgets
from drawline import MyLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 生成代码为：
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # 这里改为MyLabel，因为QLabel的鼠标点击事件没有具体实现，我们需要重写这个类的鼠标点击方法
        self.label = MyLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 22, 452, 827))
        self.label.setText("")
        self.label.setObjectName("label")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setStyleSheet("QMenuBar{background-color:rgb(240,248,255);}")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 30))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.color = QtWidgets.QAction(self.menubar)
        self.color.setObjectName("color")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew1 = QtWidgets.QAction(MainWindow)
        self.actionNew1.setObjectName("actionNew1")
        self.menuOpen.addAction(self.actionNew)
        self.menuOpen.addAction(self.actionNew1)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测量局部灰度值"))
        self.menuOpen.setTitle(_translate("MainWindow", "菜单"))
        self.color.setText(_translate("MainWindow", "标注颜色"))
        self.actionNew.setText(_translate("MainWindow", "打开图片"))
        self.actionNew1.setText(_translate("MainWindow", "保存标注"))

