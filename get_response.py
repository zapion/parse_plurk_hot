#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from urllib import urlencode as encode
from urllib2 import *
from BeautifulSoup import BeautifulSoup

data = open('./data','r')
response = open('./response_data','w')
page = re.findall( '回應" href="http://www.plurk.com/p/[\w]*"', data.read())

for p in page:
    url = re.search('href="(.*)"', p).group(1)
    #print url

    content = urlopen(Request(url)).read()
    soup = BeautifulSoup(content)
    lis = soup.findAll('li').size()
    response.write(str(lis))
    break
