import urllib2
import urllib
import json
from multiprocessing import Queue, Process
import multiprocessing
import time

start = time.time()
q = Queue()
url = 'http://www.jndata.gov.cn/data/catalog/catalog.do?method=GetCatalog'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
data = {"start":0, "length":10, "pageLength":10}
data = urllib.urlencode(data)
request = urllib2.Request(url, data=data, headers=header)
res = urllib2.urlopen(request)
dic = json.loads(res.read())

cata_id_list = []
for i in dic['data']:
    cata_id_list.append(i["cata_id"])

fields = set()
url = 'http://www.jndata.gov.cn/data/catalog/catalogDetail.do?method=GetDownLoadInfo'
for cata_id in cata_id_list:
    data = {"cata_id":cata_id, "conf_type": 2}
    data = urllib.urlencode(data)
    request = urllib2.Request(url, data=data, headers=header)
    res = urllib2.urlopen(request)
    res = json.loads(res.read())
    for i in res['data']:
        down_url = 'http://www.jndata.gov.cn/data/catalog/catalogDetail.do?method=getFileDownloadAddr&fileId=%s' % i['fileId']
        if i['fileName'].endswith('json'):
            fields.add((i['fileName'], down_url))

for filename, down_url in fields:
    res = urllib2.urlopen(down_url)
    with open(filename+'.zip', 'wb') as f:
        f.write(res.read())

print time.time() - start








# res = urllib2.urlopen(request)
# print res.read()

