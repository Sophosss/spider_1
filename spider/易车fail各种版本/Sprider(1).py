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
        infoItem = crawlDetail(item[0],item[1])
        jsonInfo.append(infoItem)
    print(jsonInfo)
    json.dumps(jsonInfo)


def crawlDetail(param1,param2):
    jsonInfo = {}
    url = "https://price.m.yiche.com/ajax/GetSearchByCsInfo.ashx?spell="+param1+"&source="
    response = requests.get(url)
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html,"html.parser")

    titleReg = re.compile("<div class=\"tt-small\"><span>(.*?)</span></div>")
    titleRegSearch = re.findall(titleReg,html)
    allItem = soup.find_all("div", attrs={'class': 'pic-txt-h'})
    dataList = []
    i = 0
    for title in titleRegSearch:
        item = str(allItem[i])
        dataReg = re.compile('<div class="c-box"><h4>(.*?)</h4><p><strong>(.*?)-(.*?)万</strong></p></div>')
        dataRegSearch = re.findall(dataReg,item)

        hrefReg = re.compile('<a class="imgbox-2" href="(.*?)">')
        hrefRegSearch = re.findall(hrefReg,item)

        try:
            url = "https://price.m.yiche.com"+hrefRegSearch[0]
            dataDictItem = {"url":url,title:{"name":dataRegSearch[0][0],"min":dataRegSearch[0][1],"max":dataRegSearch[0][2]}}
        except:
            continue
        dataList.append(dataDictItem)
        i+=1
    jsonInfo = {'code':str(param1),'data':dataList}
    # print({str(param1):jsonInfo})
    return {str(param1):jsonInfo}


if __name__ == "__main__":
    crawlHome()