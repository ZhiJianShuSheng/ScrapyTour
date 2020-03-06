#!/usr/bin/python
#-*- coding: utf-8 -*-
import codecs
import json


class JsonWriterPipeline(object):
    def __init__(self):
        # 可选实现，做参数初始化等
        # doing something
        self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。

        line = json.dumps(dict(item)) + "\n"
        # self.file.write(line.decode('unicode_escape'))
        self.file.write(line)

        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。
        print('')

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
        self.file.close()



