# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time
import numpy as np

class ScrapyDemoPipeline(object):

    def __init__(self):
        self.fh = open("items.txt", "w")


    def process_item(self, item, spider):
        '''
        print(item["cardName"])
        print(item["enName"])
        print(item["jpName"])
        print(item["imgId"])
        print(item["rare"])
        print(item["cardNumber"])
        '''
        print(item["price"])
        print(item["pricelist"])
        print(item["rare"])
        print(item['cardname'])

        print("-----------")


        self.fh.write(str(item["price"])+"\',\'"+item["pricelist"]+"\',\'"+item['cardname']+"\',\'"+item["rare"]+"\n")
        '''
        if len(item["rare"].split(',')) > 1:
            b=time.time()
            v = int(b)
            n = np.random.randint(1, 10000000)
            w = b* np.power(10, 7) - v * np.power(10, 7) + n
            m = int(w)
            for u in item["rare"].split(','):
                k = time.time()
                p = int(k)
                l = np.random.randint(1, 10000000)
                q = k * np.power(10, 7) - p * np.power(10, 7) + l
                j = int(q)
                self.fh.write("INSERT INTO `new_monster` VALUES(\'"+str(j)+'\",\''+str(m)+'\',\''
                              +item["cardNumber"]+"\',\'"+item["packageName"] +"\',\'"+item["cardName"]+"\',\'" +item["enName"] +"\',\'"
                                               +item["jpName"]+"\',\'"+item["cardName"]+"\',\'" + item["imgId"] +"\',\'"+u + '\')；'+"\n")

        else:
            b = time.time()
            v = int(b)
            n = np.random.randint(1, 10000000)
            w = b * np.power(10, 7) - v * np.power(10, 7) + n
            m = int(w)

            k = time.time()
            p = int(k)
            l = np.random.randint(1, 10000000)
            q = k * np.power(10, 7) - p * np.power(10, 7) + l
            j = int(q)
            self.fh.write("INSERT INTO `new_monster` VALUES("+str(j)+'\",\''+str(m)+'\',\''
                              + item["cardNumber"] + "\',\'"+item["packageName"] +"\',\'" + item[
                              "cardName"] + "\',\'" + item["enName"] + "\',\'"
                          + item["jpName"]+"\',\'"+item["cardName"]+ "\',\'" + item["imgId"] + "\',\'"+ item["rare"] + '\')；'+"\n")
        '''
        return item

def close_spider(self, spider):
    self.fh.close()