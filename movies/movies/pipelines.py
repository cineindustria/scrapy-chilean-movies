# -*- coding: utf-8 -*-
import json
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MoviesPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):

	def __init__(self):
		self.file = codecs.open('movies.json', 'w', encoding='utf-8')
		self.movieList = []

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		item['name'] = ''.join(item['name'])
		item['year'] = ''.join(item['year'])
		item['duration'] = ''.join(item['duration'])
		item['format'] = ''.join(item['format'])
		item['type'] = ''.join(item['type'])
		line = dict(item)
		self.movieList.append(line)
		return item

	def close_spider(self, spider):
		movieListJSON = json.dumps(self.movieList, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
		self.file.write(movieListJSON)
		self.file.close()