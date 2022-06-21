import json
import random
from .tool import HeadersTool
from typing import *
from .user_agent import user_agent
from box import Box


class Headers(HeadersTool):
    @staticmethod
    def content_length(data: Dict):
        """计算 data 长度"""
        return len(json.dumps(data, separators=(',', ':'), ensure_ascii=False))

    def user_agent(self,
                   browser_type: Optional[str] = None,
                   random_mode: Optional[bool] = False,
                   ):
        """
        随机生成请求头
        :param browser_type: 浏览器类型
        :param random_mode: 随机模式
        :return:
        """
        if random_mode:
            ua = Box(user_agent)
            browser = random.choice(['chrome', 'opera', 'firefox', 'internetexplorer', 'safari'])
            return random.choice(ua.browsers[browser])
        if browser_type == 'postman':
            return 'PostmanRuntime/7.29.0'
        if browser_type is not None:
            ua = Box(user_agent)
            return random.choice(ua.browsers[browser_type])
