import json

from _abstract import AbstractUploader

class ZhiqiuUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://zhiqiu.baidu.com/imcswebchat/api/file/upload'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['url']