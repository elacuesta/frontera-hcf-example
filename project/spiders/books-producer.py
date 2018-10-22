# -*- coding: utf-8 -*-
from urllib.parse import urlparse

from scrapy import Spider


class ProducerBooksSpider(Spider):
    name = 'books-producer'
    start_urls = ['http://books.toscrape.com']

    frontera_settings = {
        'HCF_PROJECT_ID': 353761,
        'HCF_PRODUCER_FRONTIER': 'book_links',
        'HCF_PRODUCER_SLOT_PREFIX': 'books',
        'HCF_PRODUCER_NUMBER_OF_SLOTS': 4,
        'HCF_PRODUCER_BATCH_SIZE': 300,
    }

    def parse(self, response):
        self.logger.info('Extracting links from %s', response.url)
        for book_link in response.css('article.product_pod h3 a::attr(href)').getall():
            fp = urlparse(book_link).path
            yield response.follow(book_link, meta={'cf_store': True, 'frontier_fingerprint': fp})
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page)
