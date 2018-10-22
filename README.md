# Sample project: using [scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) with [hcf-backend](https://github.com/scrapinghub/hcf-backend)

### Producer spider
```
$ scrapy crawl books-producer
2018-10-22 15:06:42 [scrapy.utils.log] INFO: Scrapy 1.5.0 started (bot: project)
(...)
2018-10-22 15:06:43 [scrapy.core.engine] INFO: Spider opened
2018-10-22 15:06:43 [manager] INFO: --------------------------------------------------------------------------------
2018-10-22 15:06:43 [manager] INFO: Starting Frontier Manager...
2018-10-22 15:06:43 [manager] INFO: Frontier Manager Started!
2018-10-22 15:06:43 [manager] INFO: --------------------------------------------------------------------------------
2018-10-22 15:06:43 [hcf_backend.backend] INFO: HCF project: 353761
2018-10-22 15:06:43 [hcf_backend.backend] INFO: HCF producer: book_links/books[0-3]
2018-10-22 15:06:43 [hcf_backend.backend] INFO: HCF consumer: NO
2018-10-22 15:06:43 [scrapy_frontera.scheduler] INFO: Starting frontier
2018-10-22 15:06:43 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2018-10-22 15:06:43 [books-producer] INFO: Extracting links from http://books.toscrape.com
2018-10-22 15:06:44 [books-producer] INFO: Extracting links from http://books.toscrape.com/catalogue/page-2.html
2018-10-22 15:06:44 [books-producer] INFO: Extracting links from http://books.toscrape.com/catalogue/page-3.html
(...)
2018-10-22 15:07:01 [books-producer] INFO: Extracting links from http://books.toscrape.com/catalogue/page-50.html
2018-10-22 15:07:01 [scrapy.core.engine] INFO: Closing spider (finished)
2018-10-22 15:07:01 [scrapy_frontera.scheduler] INFO: Finishing frontier (finished)
2018-10-22 15:07:07 [hcf_backend.backend] INFO: Flushing 1000 link(s) to all slots
2018-10-22 15:07:07 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 17180,
 'downloader/request_count': 50,
 'downloader/request_method_count/GET': 50,
 'downloader/response_bytes': 299620,
 'downloader/response_count': 50,
 'downloader/response_status_count/200': 50,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2018, 10, 22, 18, 7, 7, 933629),
 'frontera/links_extracted_count': 1000,
 'hcf/producer/book_links/books0/total_links': 255,
 'hcf/producer/book_links/books1/total_links': 250,
 'hcf/producer/book_links/books2/total_links': 246,
 'hcf/producer/book_links/books3/total_links': 249,
 'hcf/producer/book_links/new_links': 1000,
 'hcf/producer/book_links/total_links': 1000,
 'log_count/INFO': 67,
 'memusage/max': 54734848,
 'memusage/startup': 54734848,
 'request_depth_max': 50,
 'response_received_count': 50,
 'scheduler/dequeued': 50,
 'scheduler/dequeued/memory': 50,
 'scheduler/enqueued': 50,
 'scheduler/enqueued/memory': 50,
 'start_time': datetime.datetime(2018, 10, 22, 18, 6, 43, 158343)}
2018-10-22 15:07:07 [scrapy.core.engine] INFO: Spider closed (finished)
```


### Counting links
```
$ hcfpal.py count 353761 book_links
Counting requests in slots for frontier "book_links", project 353761:
	books0: 255
	books1: 250
	books2: 246
	books3: 249
	-------------------------
	Total count: 1,000
	Not-empty slots: 4
```


### Consumer spider
```
$ scrapy crawl books-consumer -o books.json
2018-10-22 15:11:11 [scrapy.utils.log] INFO: Scrapy 1.5.0 started (bot: project)
(...)
2018-10-22 15:11:11 [scrapy.core.engine] INFO: Spider opened
2018-10-22 15:11:11 [manager] INFO: --------------------------------------------------------------------------------
2018-10-22 15:11:11 [manager] INFO: Starting Frontier Manager...
2018-10-22 15:11:12 [manager] INFO: Frontier Manager Started!
2018-10-22 15:11:12 [manager] INFO: --------------------------------------------------------------------------------
2018-10-22 15:11:12 [hcf_backend.backend] INFO: HCF project: 353761
2018-10-22 15:11:12 [hcf_backend.backend] INFO: HCF producer: NO
2018-10-22 15:11:12 [hcf_backend.backend] INFO: HCF consumer: book_links/books0
2018-10-22 15:11:12 [scrapy_frontera.scheduler] INFO: Starting frontier
2018-10-22 15:11:12 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2018-10-22 15:11:13 [hcf_backend.backend] INFO: Reading 100 request(s) from batch 001669cf581a400004
2018-10-22 15:11:13 [hcf_backend.backend] INFO: Reading 100 request(s) from batch 001669cf581a40000400
2018-10-22 15:11:13 [hcf_backend.backend] INFO: Reading 55 request(s) from batch 001669cf581a40000401
2018-10-22 15:11:21 [scrapy.core.engine] INFO: Closing spider (finished)
2018-10-22 15:11:21 [scrapy_frontera.scheduler] INFO: Finishing frontier (finished)
2018-10-22 15:11:21 [scrapy.extensions.feedexport] INFO: Stored json feed (255 items) in: books.json
2018-10-22 15:11:21 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 98684,
 'downloader/request_count': 255,
 'downloader/request_method_count/GET': 255,
 'downloader/response_bytes': 1133894,
 'downloader/response_count': 255,
 'downloader/response_status_count/200': 255,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2018, 10, 22, 18, 11, 21, 173335),
 'frontera/returned_requests_count': 255,
 'hcf/consumer/book_links/books0/batches': 3,
 'hcf/consumer/book_links/books0/requests': 255,
 'item_scraped_count': 255,
 'log_count/INFO': 20,
 'memusage/max': 55107584,
 'memusage/startup': 55107584,
 'response_received_count': 255,
 'scheduler/dequeued': 255,
 'scheduler/dequeued/memory': 255,
 'scheduler/enqueued': 255,
 'scheduler/enqueued/memory': 255,
 'start_time': datetime.datetime(2018, 10, 22, 18, 11, 12, 86973)}
2018-10-22 15:11:21 [scrapy.core.engine] INFO: Spider closed (finished)
```
