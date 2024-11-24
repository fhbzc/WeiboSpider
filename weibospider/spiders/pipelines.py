
# -*- coding: utf-8 -*-
import datetime
import json
import os.path
import time


class JsonWriterPipeline(object):
    """
    写入json文件的pipline
    """

    def __init__(self):
        self.file = None
        if not os.path.exists('../output'):
            os.mkdir('../output')

    def process_item(self, item, spider):
        """
        处理item
        """
        if not self.file:
            now = datetime.datetime.now()
            if spider.save_dir is not None:
                file_name = spider.save_dir
            else:
                if spider.name == 'tweet_spider_by_keyword':

                    file_name = spider.name + "_" + spider.keyword + '_' + spider.start_time_str + '_' + spider.end_time_str + now.strftime("%Y%m%d%H%M%S") + '.jsonl'
                
                else:
                    assert False
                    file_name = spider.name + "_" + spider.keyword  + now.strftime("%Y%m%d%H%M%S") + '.jsonl'
                    
            self.file = open(f'../output/{file_name}', 'wt', encoding='utf-8')
        item['crawl_time'] = int(time.time())
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        self.file.flush()
        return item