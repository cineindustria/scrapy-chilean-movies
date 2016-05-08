# -*- coding: utf-8 -*-
import scrapy


class CinechileSpider(scrapy.Spider):
    name = "cinechile"
    allowed_domains = ["cinechile.cl"]
    start_urls = (
        'http://www.cinechile.cl/',
    )

    def parse(self, response):
        pass
