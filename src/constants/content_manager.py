import json

class ContentManager:
    def __init__(self):
        self.title = "8J+GkyBHaXRIdWIgLSBNYXRpbkdoYW5iYXJpIPCfg48="

    @staticmethod
    def get_v2ray(title: str = None) -> str:
        with open(f'src/constants/fixed-v2ray', 'r') as file:
            content = file.read()
            if title:
                content = content.replace('%TITLE%', title)
            return content
