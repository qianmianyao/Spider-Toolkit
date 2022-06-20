from abc import abstractmethod, ABCMeta
from typing import *


class HeadersTool(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def content_length(self):
        """计算 post 中 data 的长度"""
        pass


