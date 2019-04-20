# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
from multiprocessing import Queue, Process
import multiprocessing
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
start = time.time()
q = Queue()

ddd = [
{"brand_id": "33"},
{"brand_id": "35"},
{"brand_id": "34"},
{"brand_id": "117"},
{"brand_id": "276"},
{"brand_id": "36"},
{"brand_id": "14"},
{"brand_id": "15"},
{"brand_id": "38"},
{"brand_id": "75"},
{"brand_id": "120"},
{"brand_id": "13"},
{"brand_id": "40"},
{"brand_id": "27"},
{"brand_id": "39"},
{"brand_id": "95"},
{"brand_id": "173"},
{"brand_id": "231"},
{"brand_id": "154"},
{"brand_id": "203"},
{"brand_id": "79"},
{"brand_id": "208"},
{"brand_id": "140"},
{"brand_id": "143"},
{"brand_id": "37"},
{"brand_id": "271"},
{"brand_id": "301"},
{"brand_id": "333"},
{"brand_id": "76"},
{"brand_id": "77"},
{"brand_id": "163"},
{"brand_id": "196"},
{"brand_id": "299"},
{"brand_id": "294"},
{"brand_id": "1"},
{"brand_id": "165"},
{"brand_id": "32"},
{"brand_id": "113"},
{"brand_id": "259"},
{"brand_id": "169"},
{"brand_id": "81"},
{"brand_id": "41"},
{"brand_id": "187"},
{"brand_id": "142"},
{"brand_id": "280"},
{"brand_id": "326"},
{"brand_id": "3"},
{"brand_id": "8"},
{"brand_id": "42"},
{"brand_id": "11"},
{"brand_id": "96"},
{"brand_id": "141"},
{"brand_id": "197"},
{"brand_id": "282"},
{"brand_id": "82"},
{"brand_id": "152"},
{"brand_id": "112"},
{"brand_id": "108"},
{"brand_id": "313"},
{"brand_id": "329"},
{"brand_id": "304"},
{"brand_id": "116"},
{"brand_id": "181"},
{"brand_id": "91"},
{"brand_id": "86"},
{"brand_id": "97"},
{"brand_id": "87"},
{"brand_id": "260"},
{"brand_id": "220"},
{"brand_id": "164"},
{"brand_id": "245"},
{"brand_id": "150"},
{"brand_id": "24"},
{"brand_id": "267"},
{"brand_id": "184"},
{"brand_id": "43"},
{"brand_id": "336"},
{"brand_id": "85"},
{"brand_id": "25"},
{"brand_id": "46"},
{"brand_id": "44"},
{"brand_id": "84"},
{"brand_id": "83"},
{"brand_id": "119"},
{"brand_id": "145"},
{"brand_id": "210"},
{"brand_id": "270"},
{"brand_id": "151"},
{"brand_id": "175"},
{"brand_id": "297"},
{"brand_id": "319"},
{"brand_id": "47"},
{"brand_id": "9"},
{"brand_id": "101"},
{"brand_id": "219"},
{"brand_id": "214"},
{"brand_id": "109"},
{"brand_id": "199"},
{"brand_id": "224"},
{"brand_id": "100"},
{"brand_id": "156"},
{"brand_id": "52"},
{"brand_id": "49"},
{"brand_id": "53"},
{"brand_id": "51"},
{"brand_id": "279"},
{"brand_id": "78"},
{"brand_id": "54"},
{"brand_id": "10"},
{"brand_id": "48"},
{"brand_id": "80"},
{"brand_id": "88"},
{"brand_id": "241"},
{"brand_id": "50"},
{"brand_id": "124"},
{"brand_id": "89"},
{"brand_id": "118"},
{"brand_id": "204"},
{"brand_id": "335"},
{"brand_id": "318"},
{"brand_id": "58"},
{"brand_id": "20"},
{"brand_id": "57"},
{"brand_id": "56"},
{"brand_id": "129"},
{"brand_id": "168"},
{"brand_id": "55"},
{"brand_id": "130"},
{"brand_id": "213"},
{"brand_id": "60"},
{"brand_id": "146"},
{"brand_id": "59"},
{"brand_id": "332"},
{"brand_id": "61"},
{"brand_id": "308"},
{"brand_id": "62"},
{"brand_id": "26"},
{"brand_id": "122"},
{"brand_id": "222"},
{"brand_id": "312"},
{"brand_id": "235"},
{"brand_id": "63"},
{"brand_id": "19"},
{"brand_id": "174"},
{"brand_id": "296"},
{"brand_id": "337"},
{"brand_id": "103"},
{"brand_id": "67"},
{"brand_id": "68"},
{"brand_id": "65"},
{"brand_id": "155"},
{"brand_id": "45"},
{"brand_id": "69"},
{"brand_id": "238"},
{"brand_id": "162"},
{"brand_id": "149"},
{"brand_id": "205"},
{"brand_id": "269"},
{"brand_id": "66"},
{"brand_id": "90"},
{"brand_id": "133"},
{"brand_id": "202"},
{"brand_id": "161"},
{"brand_id": "70"},
{"brand_id": "114"},
{"brand_id": "283"},
{"brand_id": "167"},
{"brand_id": "284"},
{"brand_id": "192"},
{"brand_id": "291"},
{"brand_id": "102"},
{"brand_id": "99"},
{"brand_id": "12"},
{"brand_id": "71"},
{"brand_id": "72"},
{"brand_id": "306"},
{"brand_id": "185"},
{"brand_id": "98"},
{"brand_id": "275"},
{"brand_id": "324"},
{"brand_id": "73"},
{"brand_id": "110"},
{"brand_id": "111"},
{"brand_id": "144"},
{"brand_id": "298"},
{"brand_id": "263"},
{"brand_id": "286"},
{"brand_id": "307"},
{"brand_id": "93"},
{"brand_id": "232"},
{"brand_id": "317"},
{"brand_id": "94"},
{"brand_id": "22"},
{"brand_id": "74"},
{"brand_id": "206"},
{"brand_id": "182"}
]

newusers = dict()
for ud in ddd:
    newusers[ud.pop('brand_id')] = ud
# print newusers


for key in newusers.keys():
        # print key

        url = 'https://car.m.autohome.com.cn/ashx/GetSeriesByBrandId.ashx?r=6s&b=' + str(key)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        request = urllib2.Request(url, headers=header)
        res = urllib2.urlopen(request)
        dic = json.loads(res.read())
        dic1 = dic['result']['allSellSeries']
        last = json.dumps(dic1, encoding='UTF-8', ensure_ascii=False)
        print last
        # with open('file.json', "w") as f:
        #     f.write(last)
        #     f.close()

        # json.dump(dic['result']['allSellSeries'],open('file.json',"w"),ensure_ascii=False,)
# fields = set()
# url = 'http://www.jndata.gov.cn/data/catalog/catalogDetail.do?method=GetDownLoadInfo'
# for cata_id in cata_id_list:
#     data = {"cata_id":cata_id, "conf_type": 2}
#     data = urllib.urlencode(data)
#     request = urllib2.Request(url, data=data, headers=header)
#     res = urllib2.urlopen(request)
#     res = json.loads(res.read())
#     for i in res['data']:
#         down_url = 'http://www.jndata.gov.cn/data/catalog/catalogDetail.do?method=getFileDownloadAddr&fileId=%s' % i['fileId']
#         if i['fileName'].endswith('json'):
#             fields.add((i['fileName'], down_url))

#
print time.time() - start
