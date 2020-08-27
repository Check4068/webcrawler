import scrapy
from scrapy_demo.CardItems import CardItem
from scrapy.http import Request
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

Package = {1: ['ETCO-JP0', 'ETCO-JP00','ETCO-JP001', 80, 0],
           2: ['20PP-JP0', '20PP-JP00','20PP-JP001', 20, 0],
           3: ['20TP-JP1', '20TP-JP10','20TP-JP101', 16, 0],
           4: ['20CP-JPF', '20CP-JPF0','20CP-JPF01', 10, 0],
           5: ['JF20-JP0', 'JF20-JP00','JF20-JP001', 5, 0],
           6: ['LGB1-JP0', 'LGB1-JP00','LGB1-JP001', 48, 0],
           7: ['LGB1-JPS', 'LGB1-JPS0','LGB1-JPS01', 3, 0],
           8: ['SD37-JP0', 'SD37-JP00','SD37-JP001', 44, 0],
           9: ['SD37-JPP', 'SD37-JPP0','SD37-JPP01', 5, 0],
           10: ['LVP3-JP0', 'LVP3-JP00','LVP3-JP001', 100, 0],
           11: ['IGAS-JP0', 'IGAS-JP00','IGAS-JP000', 81, -1],
           12: ['SR09-JP0', 'SR09-JP00','SR09-JP001', 42, 0],
           13: ['19TP-JP4', '19TP-JP40','19TP-JP401', 16, 0],
           14: ['EP19-JP0', 'EP19-JP00','EP19-JP001', 70, 0],
           15: ['LVDS-JPA', 'LVDS-JPA0','LVDS-JPA01', 10, 0],
           16: ['LVDS-JPB', 'LVDS-JPB0','LVDS-JPB01', 10, 0],
           17: ['20CP-JPT', '20CP-JPT0','20CP-JPT01', 10, 0],
           18: ['DBMF-JP0', 'DBMF-JP00','DBMF-JP001', 45, 0],
           19: ['CHIM-JP0', 'CHIM-JP00','CHIM-JP001', 80, 0],
           20: ['19TP-JP3', '19TP-JP30','19TP-JP301', 16, 0],
           21: ['SD36-JP0', 'SD36-JP00', 'SD36-JP001', 41, 0],
           22: ['SD36-JPP', 'SD36-JPP0', 'SD36-JPP01', 5, 0],
           23: ['19SP-JP6', '19SP-JP60', '19SP-JP601', 10, 0],
           24: ['DP22-JP0', 'DP22-JP00', 'DP22-JP000', 56, -1],
           25: ['CP19-JP0', 'CP19-JP00', 'CP19-JP000', 46, -1],
           26: ['YMAB-JP0', 'YMAB-JP00', 'YMAB-JP001', 1, 0],
           27: ['19PR-JP0', '19PR-JP00', '19PR-JP001', 12, 0],
           28: ['RIRA-JP0', 'RIRA-JP00', 'RIRA-JP001', 80, 0],
           29: ['19TP-JP2', '19TP-JP20', '19TP-JP201', 16, 0],
           30: ['ST19-JP0', 'ST19-JP00', 'ST19-JP001', 45, 0],
           31: ['19SP-JP5', '19SP-JP50', '19SP-JP501', 10, 0],
           32: ['SR08-JP0', 'SR08-JP00', 'SR08-JP001', 32, 0],
           33: ['DBIC-JP0', 'DBIC-JP00', 'DBIC-JP001', 45, 0],
           34: ['20TH-JPC', '20TH-JPC0', '20TH-JPC00', 100, -1],
           35: ['20CP-JPC', '20CP-JPC0', '20CP-JPC01', 10, 0],
           36: ['20CP-JPS', '20CP-JPS0', '20CP-JPS01', 10, 0],
           37: ['DANE-JP0', 'DANE-JP00', 'DANE-JP001', 80, 0],
           38: ['19TP-JP1', '19TP-JP10', '19TP-JP101', 16, 0],
           39: ['19PP-JP0', '19PP-JP00', '19PP-JP001', 20, 0],
           40: ['JF19-JP0', 'JF19-JP00', 'JF19-JP001', 5, 0],
           41: ['SSD1-JP0', 'SSD1-JP00', 'SSD1-JP001', 21, 0],
           42: ['SSD2-JP0', 'SSD2-JP00', 'SSD2-JP001', 21, 0],
           43: ['20TH-JPB', '20TH-JPB0', '20TH-JPB01', 36, 0],
           44: ['20TH-JPB', '20TH-JPBS', '20TH-JPBS1', 6, 0],
           45: ['20TH-JPB', '20TH-JPBT', '20TH-JPBT1', 6, 0],
           46: ['SD35-JP0', 'SD35-JP00', 'SD35-JP001', 40, 0],
           47: ['SD35-JPP', 'SD35-JPP0', 'SD35-JPP01', 5, 0],
           48: ['DMMD-JP0', 'DMMD-JP00', 'DMMD-JP001', 1, 0],
           49: ['LVP2-JP0', 'LVP2-JP00', 'LVP2-JP001', 100, 0],
           50: ['18SP-JP4', '18SP-JP40', '18SP-JP401', 10, 0],
           51: ['YCPC-JP0', 'YCPC-JP00', 'YCPC-JP001', 20, 0],
           52: ['DP21-JP0', 'DP21-JP00', 'DP21-JP000', 56, -1],
           53: ['18TP-JP4', '18TP-JP40', '18TP-JP401', 16, 0],
           54: ['RC03-JP0', 'RC03-JP00', 'RC03-JP001', 50, 0],}

class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = []


    def __init__(self):
        self.browser = driver
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):

        start_urls = []

        for i in range(34,33,-1):
           start_urls.append("http://www.qi-wmcard.com/card/" + Package[i][2])
        for url in start_urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        # 将我们得到的数据封装到一个 `MyspiderItem` 对象
        item = CardItem()
        #item["cardName"] = "card"
        #item["imgId"] = "1257564"
        #item["rare"] = "mormal"
        # 提取数据

        item["cardName"] = response.xpath('//span[contains(text(),"中文名称")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["enName"] = response.xpath('//span[contains(text(),"英文名称")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n", "")
        item["jpName"] = response.xpath('//span[contains(text(),"日文名称")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n", "")
        item["imgId"] = response.xpath('//span[contains(text(),"卡片密码")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["rare"] = response.xpath('//span[contains(text(),"稀有度")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["cardNumber"]=response.xpath('//span[contains(text(),"卡片编号")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["packageName"] = response.xpath('//td[@class="navigation-text"]/a[4]/text()').extract()[0]

        '''
        print(item["cardName"])
        print(item["enName"])
        print(item["jpName"])
        print(item["imgId"])
        print(item["rare"])
        '''
        # 将获取的数据交给pipelines
        yield item

        for k in range(34,33,-1):

           for u in range(Package[k][3], Package[k][4],-1):

            if len(str(u))==1:
                url = "http://www.qi-wmcard.com/card/"+Package[k][2][:-1] + str(u)
            if len(str(u))==2:
                url = "http://www.qi-wmcard.com/card/"+Package[k][2][:-2] + str(u)
            if len(str(u))==3:
                url = "http://www.qi-wmcard.com/card/"+Package[k][2][:-3] + str(u)
            yield Request(url, callback=self.parse)


