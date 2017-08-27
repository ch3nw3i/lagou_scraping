# -*- coding:utf-8 -*-
import requests
import time
import random

def post_request(url=None, para={}, headers={}):
    print 'Downloading: ' + str(para['pn'])
    req = requests.post(url, data=para, headers=headers)
    return req

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
    headers = {
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
    }

    pn = 1
    end = 31
    for x in range(pn, end, 1):
        para = {
            'first': 'true',
            'kd': 'Python',
            'pn': pn
        }
        req = post_request(url, para, headers)
        path = 'D://GitHub//lagou_scraping//Python_search_result//'
        f = open(path + para['kd'] + '-' + str(para['pn']) + '.json', 'wb')
        f.write(req.content)
        f.close()
        time.sleep(random.randint(3, 8))
        pn = pn + 1