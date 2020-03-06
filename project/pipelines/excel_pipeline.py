from openpyxl import Workbook

class ExecelPipeLine(object):  # 设置工序一
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(['新闻标题', '新闻链接', '来源网站', '发布时间', '相似新闻', '是否含有网站名'])


    def process_item(self, item, spider):  # 工序具体内容
        # 把数据中每一项整理出来
        line = [item['title'], item['link'], item['source'], item['pub_date'], item['similar'], item['in_title']]
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('./xxxx.xlsx')  # 保存xlsx文件
        return item