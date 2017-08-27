# -*- encoding: utf-8 -*-
import json
def read_json(path):
    f = open(path)
    dictory = json.load(f, encoding='utf-8')
    return dictory

if __name__ == "__main__":
    pn = 1
    jobList = []
    for x in range(pn, 31, 1):
        path = 'D://GitHub//lagou_scraping//Python_search_result//Python-' + str(pn) + '.json'
        f = open(path)
        dictory = json.load(f, encoding='utf-8')
        for result in dictory['content']['positionResult']['result']:
            positionId = result['positionId']
            url = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'
            jobList.append(url)
    f = open('d://Github//lagou_scraping//jobList.txt', 'wb')
    for job in jobList:
        f.write(job)
        f.write('\n')
    f.close()