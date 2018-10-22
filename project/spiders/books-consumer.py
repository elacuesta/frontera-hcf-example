# -*- coding: utf-8 -*-
from scrapy import Spider


class ConsumerBooksSpider(Spider):
    name = 'books-consumer'

    frontera_settings = {
        'HCF_PROJECT_ID': 353761,
        'HCF_CONSUMER_FRONTIER': 'book_links',
        'HCF_CONSUMER_SLOT': 'books0',
    }

    def parse(self, response):
        return {
            'url': response.url,
            'title': response.css('h1::text').get(),
            'price': float(response.css('p.price_color::text').re_first(r'(\d+.?\d*)')),
        }
