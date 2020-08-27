# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time
import numpy as np
import pandas as pd
import xlsxwriter
import xlwt
import xlrd


class ScrapyDemoPipeline(object):

    def __init__(self):

        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet('My Sheet',cell_overwrite_ok=True)
        self.worksheet.write(0, 0, "JPName")
        self.worksheet.write(0, 1, "rare")

    def process_item(self, item, spider):
        '''
        print(item["cardName"])
        print(item["enName"])
        print(item["jpName"])
        print(item["imgId"])
        print(item["rare"])
        print(item["cardNumber"])

        print("-----------")
        '''


        if "\'" in item["enName"]:
            i=item["enName"].replace('\'','\\\'')
        else:
            i=item["enName"]
        self.workbook.save('example2.xlsx')
        self.data = xlrd.open_workbook('example2.xlsx')
        table = self.data.sheets()[0]
        i = table.nrows
        print(i)
        self.worksheet.write(i, 0, item["jpName"].strip().replace("·", "・"))


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
                

                self.workbook.save('example2.xlsx')
                self.data = xlrd.open_workbook('example2.xlsx')
                table = self.data.sheets()[0]
                i = table.nrows
                print(i)
                print(u)
                self.worksheet.write(i, 0, item["jpName"].strip().replace("·","・") )
                self.worksheet.write(i, 1, u)
            
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
                '''



        return item

def close_spider(self, spider):
     self.fh.close()



