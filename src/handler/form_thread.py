# -*- coding:utf-8 -*-
# Author: 廿二月的天
import os
import threading
from pathlib import Path

from PyQt5.QtCore import QThread, pyqtSignal

from handler.outfit_clash import OutfitClash


class FormThread(QThread):
    """
    业务逻辑线程
    """
    trigger = pyqtSignal(int)

    def __init__(self):
        super(FormThread, self).__init__()
        self.__source_path = None
        self.__new_path = None
        self.__queue = None
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()

    def set_source_path(self, source_path):
        self.__source_path = source_path

    def set_new_path(self, new_path):
        self.__new_path = new_path

    def set_queue(self, queue):
        self.__queue = queue

    def run(self):
        """
        启动线程函数
        :return:
        """

        outfit_clash = OutfitClash()
        i = 0
        for root, dirs, files in os.walk(self.__source_path):
            for name in files:
                prefix = os.path.splitext(name)[-1][1:]
                if prefix == "jpg" or prefix == "gif" or prefix == "jpeg" or prefix == "png":
                    file_path = Path(os.path.join(self.__source_path, name)).as_posix()
                    new_file_path = Path(os.path.join(self.__new_path, name)).as_posix()
                    plt = outfit_clash.start(file_path)
                    plt.savefig(new_file_path)
                    i = i + 1

        self.__queue.put(i)
        self.trigger.emit(1)
