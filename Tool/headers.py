import json
from .tool import HeadersTool
from typing import *


class Headers(HeadersTool):

    def __init__(self,
                 data: Optional[Dict] = None
                 ):
        self.data = data

    def content_length(self):
        return len(json.dumps(self.data, separators=(',', ':'), ensure_ascii=False))
