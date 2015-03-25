import requests
from lxml import html
from DataBaseCl import *


class Parser(object):

    def __init__(self, request_to_find):
        self.request_to_find = request_to_find

    def make_request(self):
        headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"}
        data = {'text': self.request_to_find, 'lr': '51'}
        page = requests.get('http://yandex.ru/yandsearch', params=data, headers=headers)
        self.fill_out_file('log',page.text.encode('utf-8'))
        return page.text

    def parse_response(self):
        response = self.make_request()
        root = html.fromstring(response)
        titles = [title.text_content().replace('"', '') for title in root.xpath("//a[@class = 'b-link serp-item__title-link']")]
        links = [link.text_content() for link in root.xpath("//span[@class = 'serp-url__item']")]
        content = [cont.text_content() for cont in root.xpath("//div[@class = 'serp-item__text']")]
        self.parsed_response = [' / '.join(i) for i in zip(titles, links, content)]

    def fill_out_db(self):
        db_obj = DataBaseCl()
        db_obj.db_insert('test', self.parsed_response)

    def fill_out_file(self, file_name,content):
        f=open(file_name,'w')
        f.write(content)
        f.close()


req = "test"
parser = Parser(req)
parser.parse_response()
parser.fill_out_db()