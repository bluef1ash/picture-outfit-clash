# -*- coding:utf-8 -*-
#  Author: 廿二月的天
import sys
from PyQt5 import QtWidgets
from view.main_view import MainView

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = MainView()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
