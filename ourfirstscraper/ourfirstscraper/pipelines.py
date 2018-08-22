# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from ourfirstscraper.items import ConcertItem
from ourfirstscraper.spiders.usana import *
import json
import sqlite3 as lite


con = None #db connection object - created on init and deleted on __del__

class OurfirstscraperPipeline(object):
    def __init__(self):
        self.setupDBCon()
        self.createTables()

    @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
    #     )

    # def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        # item = ConcertItem()
        # item.data = json.dumps(self.items)
        # print(item.data)
        # item.save()

    def process_item(self, item, spider):
        self.storeInDb(item) ###Trips up here! TODO figure out how to save to db
        return item

    def storeInDb(self, item):
        self.storeConcertInfoInDb(item)

    def storeConcertInfoInDb(self, item):
        self.cur.execute("INSERT INTO Concerts(\
            artist, \
            month, \
            day, \
            ticket_price)\
        VALUES( ?, ?, ?, ?)", \
        (\
            item.get('artist',""),
            item.get('month', ""),
            item.get('day',""),
            item.get('ticket_price',"")
        ))
        self.con.commit()

    def setupDBCon(self):
        self.con = lite.connect('test.db')
        self.cur = self.con.cursor()

    def __del__(self):
        self.closeDB()
    
    def createTables(self):
        self.dropConcertsTable()
        self.createConcertsTable()

    def createConcertsTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Concerts(id INTEGER PRIMARY KEY NOT NULL, \
        artist TEXT, \
        month TEXT, \
        day TEXT, \
        ticket_price TEXT)")

    def dropConcertsTable(self):
        self.cur.execute("DROP TABLE IF EXISTS Concerts")

    def closeDB(self):
        self.con.close()