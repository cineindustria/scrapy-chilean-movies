# -*- coding: utf-8 -*-
import scrapy
import sys
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

    @staticmethod
    def getMovieType(url):
        string = (url.split('/')[-1]).split('.')[0]
        if string == 'ficcion':
            typeOfMovie = 'fiction'
        elif string == 'documentales':
            typeOfMovie = 'documentary'
        elif string == 'cortometrajes':
            typeOfMovie = 'short'
        elif string == 'animacion':
            typeOfMovie = 'animation'
        return typeOfMovie
    
    def parse(self, response):
        for sel in response.xpath('//table[@id="example2"]/tbody/tr'):
            url = response.url
            filmType = self.getMovieType(url)
            item = MoviesItem()
            item['name'] = sel.xpath('td/a/text()').extract()
            item['year'] = sel.xpath('td[2]/text()').extract()
            item['duration'] = sel.xpath('td[3]/text()').extract()
            item['format'] = sel.xpath('td[4]/text()').extract()
            item['type'] = filmType
            yield item