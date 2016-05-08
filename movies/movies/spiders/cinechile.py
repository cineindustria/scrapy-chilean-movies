# -*- coding: utf-8 -*-
import scrapy


class CinechileSpider(scrapy.Spider):
    name = "cinechile"
    allowed_domains = ["cinechile.cl"]
    start_urls = (
        'http://cinechile.cl/ficcion.php',
    )

    def parse(self, response):
   #  	filename = response.url.split("/")[-2] + '.html'
   #  	with open(filename, 'wb') as f:
			# f.write(response.body)
		for sel in response.xpath('//table[@id="example2"]/tbody/tr'):
			title = sel.xpath('td/a/text()').extract()
			year = sel.xpath('td[2]/text()').extract()
			#link = sel.xpath('a/@href').extract()
			#desc = sel.xpath('text()').extract()
			print title, year
        #pass