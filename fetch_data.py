#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import re
from urllib import urlencode as encode
from urllib2 import *

out = open("./data", 'w')
p = urlopen("http://www.plurk.com/t/Taiwan#hot")
#soup = BeautifulSoup(p.read())
content = p.read()


#print soup
out.write(content)
last_offset = re.search('fetchMore\("hot", ([0-9.]*)\)', content).group(1)
print last_offset

for i in range(1,10):
    fetch = Request("http://www.plurk.com/PlurkTop/fetchPlurks")
#fetch.add_header()
    fetch.add_data(encode({'sorting':'hot', 'collection_id':2, 'offset': last_offset }))
    res = urlopen(fetch).read()
    last_offset = re.search('fetchMore\("hot", ([0-9.]*)\)', res).group(1)
    print last_offset
    out.write("i=%d:12345678901234567890123456789012345678901234567890123456789012345678901234567890\n"%i)
    out.write(res)
#soup = BeautifulSoup(res)
#print soup
