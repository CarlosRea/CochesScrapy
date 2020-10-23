# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CochesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    coche_nombre = scrapy.Field()
    coche_datos_generales = scrapy.Field()
    coche_equipamiento = scrapy.Field()
    coche_datos_tecnicos = scrapy.Field()
    pass
