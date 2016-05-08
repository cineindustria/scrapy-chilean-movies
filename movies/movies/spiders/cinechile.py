# -*- coding: utf-8 -*-
import scrapy


class CinechileSpider(scrapy.Spider):
    name = "cinechile"
    allowed_domains = ["cinechile.cl"]
    start_urls = (
        'http://cinechile.cl/ficcion.php',
    )

    def parse(self, response):
    	filename = response.url.split("/")[-2] + '.html'
    	with open(filename, 'wb') as f:
			f.write(response.body)
        #pass