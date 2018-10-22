# -*- coding: utf-8 -*-

# Scrapy settings for project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'project'

SPIDER_MODULES = ['project.spiders']
NEWSPIDER_MODULE = 'project.spiders'

LOG_LEVEL = 'INFO'

FEED_EXPORT_INDENT = 4
FEED_EXPORT_ENCODING = 'utf8'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'

CONCURRENT_REQUESTS = 32

# Frontera
FRONTERA_SETTINGS = 'project.frontera_settings'

SCHEDULER = 'scrapy_frontera.scheduler.FronteraScheduler'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_frontera.middlewares.SchedulerDownloaderMiddleware': 0,
}

SPIDER_MIDDLEWARES = {
    'scrapy_frontera.middlewares.SchedulerSpiderMiddleware': 0,
}

# Set to True if you want start requests to be redirected to frontier
# By default they go directly to scrapy downloader
# FRONTERA_SCHEDULER_START_REQUESTS_TO_FRONTIER = False

# Allows to redirect to frontier, the requests with the given callback names
# FRONTERA_SCHEDULER_REQUEST_CALLBACKS_TO_FRONTIER = []

# Spider attributes that need to be passed to the requests redirected to frontier
# Some previous callbacks may have generated some state needed for following ones.
# This setting allows to transmit that state between different jobs
# FRONTERA_SCHEDULER_STATE_ATTRIBUTES = []
