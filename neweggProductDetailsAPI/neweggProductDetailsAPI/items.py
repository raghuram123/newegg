# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeweggproductdetailsapiItem(scrapy.Item):
	brand=scrapy.Field()
	title=scrapy.Field()
	raters=scrapy.Field()
	rating=scrapy.Field()
	spec=scrapy.Field()
