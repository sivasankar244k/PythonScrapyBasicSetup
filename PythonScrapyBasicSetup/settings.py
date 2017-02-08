# -*- coding: utf-8 -*-

BOT_NAME = 'PythonScrapyBasicSetup'

SPIDER_MODULES = ['PythonScrapyBasicSetup.spiders']
NEWSPIDER_MODULE = 'PythonScrapyBasicSetup.spiders'

# maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
# timeout for processing DNS queries in seconds(float) (default: 60)
DNS_TIMEOUT = 10
# time(sec) that the downloader will wait before timing out
DOWNLOAD_TIMEOUT = 24

# use telnet console
TELNETCONSOLE_ENABLED = False

# delay for requests for the same website (default: 0)
# DOWNLOAD_DELAY = 3
# download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# maximum number of times to retry
RETRY_TIMES = 2
# HTTP response codes to retry
RETRY_HTTP_CODES = [500, 502, 503, 504]

# disable cookies
COOKIES_ENABLED = False

# downloader middlewares
DOWNLOADER_MIDDLEWARES = {
	'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
	'PythonScrapyBasicSetup.middlewares.RandomUserAgentMiddleware': 400,
    'PythonScrapyBasicSetup.middlewares.ProxyMiddleware': 410
}
