import base64


class ContentManager:
    def __init__(self):
        self.default_v2ray_title = "8J+GkyBHaXRIdWIgLSBNYXRpbkdoYW5iYXJpIPCfg48="
        self.default_v2ray_sub_title = "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYWJyaSB8IFN1Yg=="

        self.default_warp_title = "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IFdhcnAg8J+MkA=="

        self.filter_titles = {
            "vmess": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IHZtZXNzIPCfkb0=",
            "vless": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IHZsZXNzIPCfkb0=",
            "trojan": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IHRyb2phbiDwn5G9",
            "ss": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IHNzIPCfkb0=",
            "ssr": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IHNzciDwn5G9",
            "tuic": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IHR1aWMg8J+RvQ==",
            "hy2": "8J+GkyBHaXRIdWI6TWF0aW5HaGFuYmFyaSB8IGh5MiDwn5G9"
        }

    @staticmethod
    def __get_file(file_path: str, title: str = None, default: str = None) -> str:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            if title:
                content = content.replace('%TITLE%', base64.b64encode(title.encode()).decode())
            elif default:
                content = content.replace('%TITLE%', default)
        return content

    def get_warp(self, title: str = None) -> str:
        return self.__get_file(f'src/contents/fixed-warp',
                               title, self.default_warp_title)

    def get_filtered(self, title: str = None, protocol: str = None) -> str:
        return self.__get_file(f'src/contents/fixed-filtered',
                               title, self.filter_titles.get(protocol) if protocol else self.default_v2ray_title)

    def get_v2ray(self, title: str = None) -> str:
        return self.__get_file(f'src/contents/fixed-v2ray',
                               title, self.default_v2ray_title)

    def get_v2ray_sub(self, sub_id: int) -> str:
        title = str(base64.b64decode(self.default_v2ray_sub_title).decode() + str(sub_id))
        return self.get_v2ray(title)
