# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 603)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_text = QLabel(self.centralwidget)
        self.title_text.setObjectName(u"title_text")
        self.title_text.setGeometry(QRect(200, 10, 331, 51))
        font = QFont()
        font.setPointSize(18)
        self.title_text.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(410, 70, 441, 201))
        self.file_text = QLabel(self.widget)
        self.file_text.setObjectName(u"file_text")
        self.file_text.setGeometry(QRect(10, 10, 61, 21))
        self.img_path = QLineEdit(self.widget)
        self.img_path.setObjectName(u"img_path")
        self.img_path.setGeometry(QRect(80, 40, 131, 31))
        self.vedio_path = QLineEdit(self.widget)
        self.vedio_path.setObjectName(u"vedio_path")
        self.vedio_path.setGeometry(QRect(80, 90, 131, 31))
        self.camera_path = QLineEdit(self.widget)
        self.camera_path.setObjectName(u"camera_path")
        self.camera_path.setGeometry(QRect(80, 140, 131, 31))
        self.img_text = QLabel(self.widget)
        self.img_text.setObjectName(u"img_text")
        self.img_text.setGeometry(QRect(10, 40, 31, 31))
        self.vedio_text = QLabel(self.widget)
        self.vedio_text.setObjectName(u"vedio_text")
        self.vedio_text.setGeometry(QRect(10, 90, 31, 31))
        self.camera_text = QLabel(self.widget)
        self.camera_text.setObjectName(u"camera_text")
        self.camera_text.setGeometry(QRect(10, 140, 31, 31))
        self.select_file = QPushButton(self.widget)
        self.select_file.setObjectName(u"select_file")
        self.select_file.setGeometry(QRect(260, 40, 100, 32))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(400, 290, 441, 251))
        self.detect_title = QLabel(self.widget_2)
        self.detect_title.setObjectName(u"detect_title")
        self.detect_title.setGeometry(QRect(10, 0, 58, 16))
        self.time_cost = QLabel(self.widget_2)
        self.time_cost.setObjectName(u"time_cost")
        self.time_cost.setGeometry(QRect(20, 40, 58, 16))
        self.num_workers = QLabel(self.widget_2)
        self.num_workers.setObjectName(u"num_workers")
        self.num_workers.setGeometry(QRect(140, 40, 58, 16))
        self.num_helmets = QLabel(self.widget_2)
        self.num_helmets.setObjectName(u"num_helmets")
        self.num_helmets.setGeometry(QRect(10, 80, 71, 16))
        self.num_vest = QLabel(self.widget_2)
        self.num_vest.setObjectName(u"num_vest")
        self.num_vest.setGeometry(QRect(140, 80, 71, 21))
        self.if_dang = QLabel(self.widget_2)
        self.if_dang.setObjectName(u"if_dang")
        self.if_dang.setGeometry(QRect(10, 130, 111, 21))
        self.detect_result = QLineEdit(self.widget_2)
        self.detect_result.setObjectName(u"detect_result")
        self.detect_result.setGeometry(QRect(140, 130, 161, 31))
        self.area = QLabel(self.widget_2)
        self.area.setObjectName(u"area")
        self.area.setGeometry(QRect(20, 180, 58, 16))
        self.show_label = QLabel(self.centralwidget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setGeometry(QRect(10, 70, 381, 431))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 877, 24))
        self.menuSafety_detect = QMenu(self.menubar)
        self.menuSafety_detect.setObjectName(u"menuSafety_detect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSafety_detect.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_text.setText(QCoreApplication.translate("MainWindow", u"     \u57fa\u4e8eyolov11\u7684\u5de5\u4e1a\u5de5\u4eba\u5b89\u5168\u68c0\u6d4b\u7cfb\u7edf", None))
        self.file_text.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5bfc\u5165\uff1a", None))
        self.img_path.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65f6\u672a\u5bfc\u5165\u56fe\u7247", None))
        self.vedio_path.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65f6\u672a\u5bfc\u5165\u89c6\u9891", None))
        self.camera_path.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65f6\u672a\u6253\u5f00\u6444\u50cf\u5934", None))
        self.img_text.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None))
        self.vedio_text.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None))
        self.camera_text.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None))
        self.select_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.detect_title.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.time_cost.setText(QCoreApplication.translate("MainWindow", u"\u7528\u65f6", None))
        self.num_workers.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4eba\u6570\u76ee\uff1a", None))
        self.num_helmets.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u5e3d\u6570\u76ee", None))
        self.num_vest.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u670d\u6570\u76ee", None))
        self.if_dang.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u6709\u5371\u9669\u9690\u60a3\uff1a", None))
        self.detect_result.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u68c0\u6d4b.....", None))
        self.area.setText(QCoreApplication.translate("MainWindow", u"\u533a\u57df\uff1a", None))
        self.show_label.setText(QCoreApplication.translate("MainWindow", u"picture", None))
        self.menuSafety_detect.setTitle(QCoreApplication.translate("MainWindow", u"Safety_detect", None))
    # retranslateUi

