import requests
import json
import re
from bs4 import BeautifulSoup

def crawlHome():
    jsonInfo = []
    dataList = []
    list1= ['audi', 'alfaromeo', 'astonmartin', 'alpina', 'arcfox-289', 'bj', 'bmw', 'mercedesbenz', 'honda', 'buick', 'peugeot', 'bydauto', 'porsche', 'borgward', 'besturn', 'bisuqiche-263', 'shenbao', 'beiqihuansu', 'ww', 'changheauto', 'beijingjeep', 'daoda-282', 'beiqixinnengyuan', 'bjqc', 'bentley', 'cajc', 'casyc', 'changanqingxingche-281', 'changankuayue-283', 'greatwall', 'volkswagen', 'dongfengfengdu', 'dongfengfengguang', 'fs', 'fengxingauto', 'dongfengxiaokang-205', 'dongfeng-27', 'southeastautomobile', 'dodge', 'ds', 'dearcc', 'toyota', 'ford', 'fiat', 'ferrari', 'foday', 'fujianxinlongmaqichegufenyouxiangongsi', 'foton', 'faradayfuture', 'gq', 'gacne', 'qorosauto', 'sinogold', 'gmc-109', 'hafu-196', 'hama', 'hanteng', 'faw-hongqi', 'huataiautomobile', 'redstar', 'sgautomotive', 'horki', 'huasong', 'geely', 'jac', 'jauger', 'jeep', 'jetour', 'jmc', 'singulato', 'jinbei', 'kinglongmotor', 'joylongautomobile', 'traum', 'cadillac', 'kaiyi', 'chrysler', 'karry', 'zhejiangkaersen', 'kawei', 'kangdi', 'lexus', 'renult', 'lynkco', 'lincoln', 'landwind', 'landrover', 'lifanmotors', 'suzuki', 'rolls-royce', 'lamborghini', 'cf', 'leapmotor', 'mazda', 'mg-79', 'mini', 'mclaren', 'maserati', 'luxgen', 'oushang', 'acura', 'polestar', 'chery', 'venucia', 'kia', 'chautotechnology', 'isuzu', 'nissan', 'roewe', 'skoda', 'subaru', 'smart', 'siwei', 'sol', 'mitsubishi', 'maxus', 'sam', 'ssangyong', 'tesla', 'denza', 'sgmw', 'volvo', 'wey', 'weilaiqiche', 'isuzu-132', 'enranger', 'weltmeister', 'chevrolet', 'citroen', 'hyundai', 'xpeng', 'xingchi', 'infiniti', 'yusheng-258', 'ym', 'faw', 'iveco', 'yulu', 'yudo', 'zotyeauto', 'brillianceauto', 'zhidou', 'zhinuo', 'zxauto']
    for li in list1 :
        url = 'https://price.m.yiche.com/ajax/GetSearchByCsInfo.ashx?spell=' + li +'&source='
        response = requests.get(url)
        html = response.content.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        titleReg = re.compile("<div class=\"tt-small\"><span>(.*?)</span></div>")
        titleRegSearch = re.findall(titleReg, html)
        allItem = soup.find_all("div", attrs={'class': 'pic-txt-h'})

        i = -1
        for title in titleRegSearch:
            i += 1
            item = str(allItem[i])
            hrefReg = re.compile('<a class="imgbox-2" href="(.*?)">')
            hrefRegSearch = re.findall(hrefReg, item)
            dataReg = re.compile('<div class="c-box"><h4>(.*?)</h4><p><strong>(.*?)</strong></p></div>')
            dataRegSearch = re.findall(dataReg, item)
            j = -1
            for hre in hrefRegSearch:
                j += 1
                url = "https://price.m.yiche.com" + hrefRegSearch[j]
                if (dataRegSearch[j][1].count("未上市") != 0 or dataRegSearch[j][1].count("暂无") != 0):
                    min = 0
                    max = 0
                else:
                    min = dataRegSearch[j][1].split("-")[0]
                    max = dataRegSearch[j][1].split("-")[1].replace("万", "")
                dataDictItem = {'brand':li,'series':title,"name": dataRegSearch[j][0],"url": url,"min":min,"max":max}
                dataList.append(dataDictItem)
    jsonInfo = {'data': dataList}
    jsonText = json.dumps(jsonInfo)
    print(jsonText)
    # print(jsonInfo)

if __name__ == "__main__":
    crawlHome()