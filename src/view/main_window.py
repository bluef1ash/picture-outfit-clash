# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(450, 200)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        main_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(160, 130, 111, 51))
        self.start_button.setObjectName("start_button")
        self.source_path_label = QtWidgets.QLabel(self.centralwidget)
        self.source_path_label.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.source_path_label.setFont(font)
        self.source_path_label.setObjectName("source_path_label")
        self.source_path_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.source_path_line_edit.setGeometry(QtCore.QRect(130, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.source_path_line_edit.setFont(font)
        self.source_path_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.source_path_line_edit.setObjectName("source_path_line_edit")
        self.new_path_label = QtWidgets.QLabel(self.centralwidget)
        self.new_path_label.setGeometry(QtCore.QRect(10, 70, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.new_path_label.setFont(font)
        self.new_path_label.setObjectName("new_path_label")
        self.new_path_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.new_path_line_edit.setGeometry(QtCore.QRect(130, 70, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.new_path_line_edit.setFont(font)
        self.new_path_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.new_path_line_edit.setObjectName("new_path_line_edit")
        self.source_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.source_path_button.setGeometry(QtCore.QRect(350, 20, 81, 41))
        self.source_path_button.setObjectName("source_path_button")
        self.new_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_path_button.setGeometry(QtCore.QRect(350, 70, 81, 41))
        self.new_path_button.setObjectName("new_path_button")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        self.start_button.clicked.connect(main_window.close)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "淘宝图片去同款小工具"))
        self.start_button.setText(_translate("main_window", "开始运行"))
        self.source_path_label.setText(_translate("main_window", "原路径"))
        self.new_path_label.setText(_translate("main_window", "另存为路径"))
        self.source_path_button.setText(_translate("main_window", "浏览"))
        self.new_path_button.setText(_translate("main_window", "浏览"))
