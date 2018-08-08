# -*- coding: utf-8 -*-
import scrapy


class UsanaSpider(scrapy.Spider):
    name = 'usana'
    allowed_domains = ['www.usana-amp.com/events/']
    start_urls = ['https://www.usana-amp.com/events//']

    def parse(self, response):
        # extracting response
        months = response.css(".mm::text").extract()
        days = response.css(".dd::text").extract()
        artists = response.css("h2").css("a::text").extract()
        prices = response.css(".cost::text").extract()

        for event_date in zip(months,days,artists,prices):
            # create dictionary for scraped info
            scraped_info = {
                'months': event_date[0],
                'days': event_date[1],
                'artists':event_date[2],
                'ticket_prices': event_date[3]
            }
            # give scraped_info to scrapy
            yield scraped_info
