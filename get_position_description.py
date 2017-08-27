# -*- coding: utf-8 -*
import urllib2
from bs4 import BeautifulSoup

def donwload(url):
    headers = {
        'User-Agent':''
    }
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html, 'html.parser')
    return soup