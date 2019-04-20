import requests
import json
import re
from bs4 import BeautifulSoup



def crawlHome():
    jsonInfo = []
    url = 'http://price.m.yiche.com/'
    response = requests.get(url)
    html = response.content.decode("utf-8")
    tagReg = re.compile('<a href="#" dataspell=(.*?) data-action=\'car\'><span class=".*?"><img src=".*?"></span><span class="brand-name">(.*?)</span></a>')
    tagRegSearch = re.findall(tagReg,html)
    for item in tagRegSearch:
        jsonInfo.append(item[0])
    print(jsonInfo)

if __name__ == "__main__":
    crawlHome()