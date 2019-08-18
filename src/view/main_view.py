# -*- coding:utf-8 -*-
# Author: 廿二月的天
import os
from queue import Queue

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from handler.form_thread import FormThread
from view.main_window import Ui_main_window


class MainView(QtWidgets.QMainWindow, Ui_main_window):
    """
    主窗口自定义设置
    """

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.form_thread = None
        self.queue = None
        self.main_window = None

    def setupUi(self, main_window):
        super(MainView, self).setupUi(main_window)
        self.main_window = main_window
        self.main_window.setMaximumSize(self.main_window.width(), self.main_window.height())
        self.main_window.setMinimumSize(self.main_window.width(), self.main_window.height())
        self.main_window.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.source_path_button.clicked.connect(lambda: self.load_path_listener(self.source_path_line_edit))
        self.new_path_button.clicked.connect(lambda: self.load_path_listener(self.new_path_line_edit))
        self.start_button.clicked.connect(self.on_start_listener)

    def load_path_listener(self, button):
        """
        路径浏览按钮点击信号槽
        :param button
        :return:
        """
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        button.setText(directory)

    def on_start_listener(self):
        """
        开始执行按钮单击信号槽
        :return:
        """
        source_path = self.source_path_line_edit.text()
        new_path = self.new_path_line_edit.text()
        if source_path != "" and new_path != "":
            if not os.path.isdir(source_path) and not os.path.isdir(new_path):
                QtWidgets.QMessageBox.critical(self, "错误！", "原路径或者另存为路径不是文件夹！")
            else:
                self.queue = Queue()
                self.form_thread = FormThread()
                self.form_thread.set_source_path(source_path)
                self.form_thread.set_new_path(new_path)
                self.form_thread.set_queue(self.queue)
                self.form_thread.start()
                self.form_thread.trigger.connect(self.trigger)
                self.start_button.setText("正在运行")
                self.start_button.setDisabled(True)

        else:
            QtWidgets.QMessageBox.critical(self, "错误！", "原路径与另存为路径不能为空！")

    def trigger(self, return_type):
        """
        接收业务逻辑线程信号并修改UI
        :param return_type:
        :return:
        """

        if return_type == 1:
            index = self.queue.get()
            QMessageBox.information(self, "恭喜", "恭喜！本次运行共执行" + str(index) + "次")
            self.start_button.setText("开始运行")
            self.start_button.setDisabled(False)
            self.main_window.showNormal()
            self.main_window.activateWindow()
        else:
            QMessageBox.information(self, "恭喜", "并没有需要修改的条目")
