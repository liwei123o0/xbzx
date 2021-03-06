# -*- coding: utf-8 -*-

# Scrapy settings for zbzxtest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'zbzxtest'

SPIDER_MODULES = ['zbzxtest.spiders']
NEWSPIDER_MODULE = 'zbzxtest.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
# LOG_ENABLED = False
LOG_LEVEL = 'INFO'

# SPLASH_URL = 'http://192.168.48.130:8050'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS=2

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
# COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
   # 'zbzxtest.middlewares.MyCustomSpiderMiddleware': 543,
   #  'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 3,
   #  'zbzxtest.middleware.HttpProxyMiddleware': 4,
    # 'zbzxtest.middlewares':4,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
   # 'zbzxtest.middlewares.MyCustomDownloaderMiddleware': 543,
   # 'scrapyjs.SplashMiddleware':725
# }
# DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapyjs.SplashAwareFSCacheStorage'
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'zbzxtest.pipelines.ZbzxtestPipeline': 800,
   #  'zbzxtest.pipelines.JrttPipeline':301,
   # 'zbzxtest.pipelines.PipelineGsXJ':321,
    # 'zbzxtest.pipelines.PipelineGsSAX':340,
   #  'zbzxtest.pipelines.Pipeline12312':802,
   #  'zbzxtest.pipelines.Pipelinebgcheck':303,
   #  'zbzxtest.pipelines.Pipelineccxi':304,
   #  'zbzxtest.pipelines.Pipelinelhratings':305,
   #   'zbzxtest.pipelines.Pipelinepyrating':306,
   #  'zbzxtest.pipelines.Pipelinelnqyxypgw':307,
   #  'zbzxtest.pipelines.Pipeline51jobsx':800,
     # 'zbzxtest.pipelines.Pipeline51jobsax':800,
    # 'zbzxtest.pipelines.ZbzxtestczPipeline': 309,
    # 'zbzxtest.pipelines.PipelineBcpcn':210,
    'zbzxtest.pipelines.PipelineCcgp':300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
