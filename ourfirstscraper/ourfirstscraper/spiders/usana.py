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
        ticket_links = response.css(".wraper-bottom-right.valign-wrapper").css("a::attr(href)").extract()
        
        for i in range(len(months)):
            item = ConcertItem()
            item['artist'] = artists[i].strip()
            item['month'] = months[i]
            item['day'] = days[i]
            item['ticket_link'] = ticket_links[i]
            yield { 'item': item }
        
            
            
    
    #The State Room potential spider
    #http://thestateroom.com/shows
    # response.css("h2").css("a::text").extract() -----for artists
    # response.css("h3").css("span::text").extract() -----for dates(includes Month, Day, Year)
    # response.css(".ohanah-registration-link").css("a::attr(href)").extract() ----link to buy tickets
    
    #The Depot uses client-side rendering so I can't scrape the data I want with scrapy

    # Vivint Arena
    # http://www.vivintarena.com/events?event_type=Concert
    # ----artists--- response.css(".title").css("h5::text").extract() 
    # ---specify month to get artists for that month---?? to get month 
    # response.css("#october").css(".title").css("h5::text").extract() 
    # ----days---- response.css(".date").css("em::text").extract() 
    # ----time of concert response.css(".date").css("i::text").extract() 
    # ---ticket_links,  remember when /tickets is extracted to skip it before saving other links to db
    # response.css(".tickets").css("a::attr(href)").extract() 

    # Kenley Amphitheater
    # ---artists---delete the last one because it brings up Subscription Details and not an artist
    # response.css(".entry-title").css("a::text").extract()
    # ---date---first 3 words in p tag text is the date "August 25,2018 | blah blah..."
    # response.css(".post-content").css("p::text").extract()
    # ---ticket_link--- no need to extract
    #  https://tickets.davisarts.org/

    # Sandy Amphitheater
    #  ---artists---date---time
    # response.css(".item-title::text").extract()
    # Figure out how to separately save words from that...convert each word in a list? and then pop, etc.?
    # --ticket-link-- all the same for every concert
    # https://sandyamp.com/ticket-info   is a redirect to smithtixs

    # Sundance Bluebird Concert Series
    # ---dates--- (month and day)
    # response.css("li").css("strong::text").extract()
    # ---artists--- Might require manual input...doable because only 4-5 shows during the summer. Could use .join on \n to eliminate extra space.

    


