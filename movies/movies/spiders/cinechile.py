# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem

class CinechileSpider(scrapy.Spider):
    name = "cinechile"
    allowed_domains = ["cinechile.cl"]
    start_urls = (
        'http://cinechile.cl/ficcion.php',
        'http://cinechile.cl/documentales.php',
        'http://cinechile.cl/cortometrajes.php',
        'http://cinechile.cl/animacion.php'
    )

    def parse(self, response):
        for sel in response.xpath('//table[@id="example2"]/tbody/tr'):
            item = MoviesItem()
            item['name'] = sel.xpath('td/a/text()').extract()
            item['year'] = sel.xpath('td[2]/text()').extract()
            yield item