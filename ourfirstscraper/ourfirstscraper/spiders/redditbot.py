# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.quotes.toscrape.com/page/1/']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        print(response)
        #Extracting the content using css selectors
        titles = response.css('.s5kz2p-0.bVdPMC::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,votes,times,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'comments' : item[3],
            }

            #yield or give the scraped info to scrapy
            print("This is the scraped data", scraped_info)
            yield scraped_info
        