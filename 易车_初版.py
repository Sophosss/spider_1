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

    jsonText = json.dumps({"data":jsonInfo})
    print(jsonText)


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
    i = -1
    for title in titleRegSearch:
        i += 1
        item = str(allItem[i])
        hrefReg = re.compile('<a class="imgbox-2" href="(.*?)">')
        hrefRegSearch = re.findall(hrefReg, item)
        dataReg = re.compile('<div class="c-box"><h4>(.*?)</h4><p><strong>(.*?)</strong></p></div>')
        dataRegSearch = re.findall(dataReg,item)

        if(dataRegSearch[0][1].count("未上市")!=0 or dataRegSearch[0][1].count("暂无")!=0):
            min = 0
            max = 0
        else:
            min = dataRegSearch[0][1].split("-")[0]
            max = dataRegSearch[0][1].split("-")[1].replace("万","")
        url = "https://price.m.yiche.com"+hrefRegSearch[0]
        dataDictItem = {"url":url,title:{"name":dataRegSearch[0][0],"min":min,"max":max}}
        dataList.append(dataDictItem)

    jsonInfo = {'code':str(param1),'data':dataList}
    # print({str(param1):jsonInfo})
    return {str(param1):jsonInfo}


if __name__ == "__main__":
    crawlHome()