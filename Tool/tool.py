from abc import abstractmethod, ABCMeta
from typing import *


class HeadersTool(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def content_length(*kv, **kw):
        """计算 post 中 data 的长度"""
        pass

    @staticmethod
    @abstractmethod
    def user_agent(*kv, **kw):
        """随机 user-agent """
        pass


class EncryptTool(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def url_encode(params: str):
        """url 编码"""
        pass

    @staticmethod
    @abstractmethod
    def url_decode(params: str):
        """url 解码"""
        pass

    @staticmethod
    @abstractmethod
    def md5_encode(params: Any):
        """md5 编码"""
        pass

    @staticmethod
    @abstractmethod
    def base64_encode(params: Any):
        """base64 编码"""
        pass

    @staticmethod
    @abstractmethod
    def base64_decode(params: Any):
        """base64 解码"""
        pass


