#!/usr/bin/env python
# encoding: utf-8
"""
Author: nghuyong
Mail: nghuyong@163.com
Created Time: 2019-12-07 21:27
"""
import os
import sys
import datetime
import threading
from pytz import timezone
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from spiders.tweet_by_keyword_repeat import TweetSpiderByKeywordRepeat

def run_spider():
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    deferred = runner.crawl(TweetSpiderByKeywordRepeat)
    deferred.addBoth(lambda _: check_time())

def check_time():
    if datetime.datetime.now() < dt_threshold:
        reactor.callLater(1, run_spider)
    else:
        print("Collection finished.")
        reactor.stop()

if __name__ == '__main__':
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    dt_threshold = datetime.datetime(year=2024, month=6, day=28, hour=13, minute = 30)
    print("dt_threshold",dt_threshold)
    reactor.callLater(0, run_spider)
    reactor.run()

# if __name__ == '__main__':
#     # mode = sys.argv[1]
#     os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)


#     dt_threshold = datetime.datetime(year = 2024, month = 6, day = 26, hour = 20)
#     while datetime.datetime.now() < dt_threshold:

#         process.crawl(TweetSpiderByKeywordRepeat)
#         process.start()

#         time.sleep(1)
#             