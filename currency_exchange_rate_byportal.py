# use https://portal.sw.nat.gov.tw/ api to get the exchange rate
import requests
import json
import sys

import time

year = time.strftime("%Y", time.localtime())
mon = time.strftime("%m", time.localtime())
# day = int(time.strftime("%d", time.localtime())) // 10
# day in 1-10 then = 1 , 11-20 then = 2 , 21-31 then = 3
day = int(time.strftime("%d", time.localtime())) // 10 + 1
if day == 4:
    day = 3
print("-------------------")
print(year,mon,day)

# this url will download the json file，but i dont want to do this

# url =  "https://openapi.taifex.com.tw/v1/DailyOptionsDelta"
# response = requests.get(url)
# data = response.text
# parsed = json.loads(data)

url = "https://portal.sw.nat.gov.tw/APGQ/GC331!query"
#this is parsed ?formBean.txtFileName=&formBean.jsonFileName=&formBean.guestCount=&formBean.crrnCd=&formBean.year=2023&formBean.mon=06&formBean.tenDay=2&commEmail=
formBean = {
    "formBean.txtFileName": "",
    "formBean.jsonFileName": "",
    "formBean.guestCount": "",
    "formBean.crrnCd": "",
    "formBean.year": year,
    "formBean.mon": mon,
    "formBean.tenDay": day,
    "formBean.commEmail": ""
}

# api get like this https://portal.sw.nat.gov.tw/APGQ/GC331!query?formBean.txtFileName=&formBean.jsonFileName=&formBean.guestCount=&formBean.crrnCd=&formBean.year=2023&formBean.mon=06&formBean.tenDay=2&commEmail=
response = requests.get(url, params=formBean)
response.encoding = 'utf-8'
# print(response.text)
#{"status":"ok","data":[{"UP_DAT。E":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.12469","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.12429","CRRN_CD":"ARS","ORDER_FLAG":8},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"21.04000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"20.84000","CRRN_CD":"AUD","ORDER_FLAG":7},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"6.32023","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"6.29969","CRRN_CD":"BRL","ORDER_FLAG":9},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"23.15000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"22.95000","CRRN_CD":"CAD","ORDER_FLAG":8},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"34.10000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"33.85000","CRRN_CD":"CHF","ORDER_FLAG":9},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.03815","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.03802","CRRN_CD":"CLP","ORDER_FLAG":10},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"4.31500","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"4.26500","CRRN_CD":"CNY","ORDER_FLAG":14},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"4.44060","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"4.42620","CRRN_CD":"DKK","ORDER_FLAG":2},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"33.45000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"33.05000","CRRN_CD":"EUR","ORDER_FLAG":4},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"39.08000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"38.68000","CRRN_CD":"GBP","ORDER_FLAG":2},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"3.95300","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"3.89300","CRRN_CD":"HKD","ORDER_FLAG":5},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.00207","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.00206","CRRN_CD":"IDR","ORDER_FLAG":3},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"8.54560","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"8.51782","CRRN_CD":"ILS","ORDER_FLAG":12},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.37338","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.37217","CRRN_CD":"INR","ORDER_FLAG":11},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.21940","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.21540","CRRN_CD":"JPY","ORDER_FLAG":10},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.02392","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.02384","CRRN_CD":"KRW","ORDER_FLAG":6},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"6.66780","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"6.64610","CRRN_CD":"MYR","ORDER_FLAG":4},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"2.84860","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"2.83930","CRRN_CD":"NOK","ORDER_FLAG":5},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"19.09000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"18.89000","CRRN_CD":"NZD","ORDER_FLAG":12},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"8.43339","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"8.40598","CRRN_CD":"PEN","ORDER_FLAG":13},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.54870","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.54690","CRRN_CD":"PHP","ORDER_FLAG":1},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"7.44915","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"7.42494","CRRN_CD":"PLN","ORDER_FLAG":7},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"2.92000","TEN_DAY":"3","YEAR":"2023","UP_PERSON"00","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"22.79000","CRRN_CD":"SGD","ORDER_FLAG":6},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"0.90760","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"0.86760","CRRN_CD":"THB","ORDER_FLAG":13},{"UP_DATE":null,"MON":"06","EX_RATE":"1.00000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":null,"IN_RATE":"1.00000","CRRN_CD":"TWD","ORDER_FLAG":null},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"30.76500","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"30.66500","CRRN_CD":"USD","ORDER_FLAG":1},{"UP_DATE":"2023-06-15T16:27:46","MON":"06","EX_RATE":"1.72000","TEN_DAY":"3","YEAR":"2023","UP_PERSON":"CA010","IN_RATE":"1.64000","CRRN_CD":"ZAR","ORDER_FLAG":3}],"guest":"0047395509","msg":"[執行成功]"}
# print(response.json())
print("-------------------")
json = response.json()["data"]
for i in json:
    print(i["CRRN_CD"],i["EX_RATE"],i["IN_RATE"])
print("-------------------")

#list json dict


