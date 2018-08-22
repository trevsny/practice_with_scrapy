# -*- coding: utf-8 -*-
import scrapy
# Need to figure out file path to import the Concert model in order to save to db
from ourfirstscraper.items import ConcertItem 

class UsanaSpider(scrapy.Spider):
    name = 'usana'
    allowed_domains = ['www.usana-amp.com/events/']
    start_urls = ['https://www.usana-amp.com/events//']

    def parse(self, response):
        # extracting response
        months = response.css(".mm::text").extract() #result is a list of months
        days = response.css(".dd::text").extract()
        artists = response.css("h2").css("a::text").extract()
        ticket_prices = response.css(".cost::text").extract()
        
        for i in range(len(months)):
            concert = {}
            item = ConcertItem()
            item['artist'] = artists[i]
            item['month'] = months[i]
            item['day'] = days[i]
            # item['ticket_price'] = ticket_prices[i]
            concert['newconcert'] = item
        # for artist in artists:
        #     fixed = artist.strip()
        #     # append fixed to some list ??
            
            yield concert
       

       