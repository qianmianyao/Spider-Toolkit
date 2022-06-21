from typing import Any
import hashlib
from .tool import EncryptTool
import urllib.parse
import base64


class Encrypt(EncryptTool):
    @staticmethod
    def md5_encode(params: Any):
        md5 = hashlib.md5()
        md5.update(bytes(params))
        return md5.hexdigest()

    @staticmethod
    def base64_encode(params: Any):
        return base64.b64encode(params)

    @staticmethod
    def base64_decode(params: Any):
        return base64.b64decode(params)

    @staticmethod
    def url_decode(params: str):
        return urllib.parse.urlparse(params)

    @staticmethod
    def url_encode(params: str):
        return urllib.parse.urlencode(params)
