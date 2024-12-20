import re
import sqlite3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import os
import time


def main():
    baseurl = "https://shenzhen.anjuke.com/sale/"
    datalist = getData(baseurl)
    print(datalist)
    dbpath = "price.db"
    saveData(datalist, dbpath)


def getData(baseurl):
    datalist = []
    arealist = ["nanshan", "pingshanq", "longgang", "baoan", "longhuaq", "futian", "luohu", "guangmingx", "yantian",
                "dapengxinqu"]
    carealist = ["南山", "坪山", "龙岗", "宝安", "龙华", "福田", "罗湖", "光明", "盐田", "大鹏新区"]

    for i in range(0, 10):
        url = baseurl + arealist[i] + '/'
        print(url)
        html = askURL(url)
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_="property-content"):
            data = []
            data.append(carealist[i])
            item = str(item)


            findname = r'<p\s+class="property-content-info-comm-name"[^>]*?>(.*?)<\/p>'
            name = re.search(findname, item).group(1)
            data.append(name)


            findTotalprice = r'<span\s+class="property-price-total-num"[^>]*?>(\d+.?\d*)</span>'
            totalprice = re.search(findTotalprice, item).group(1)
            data.append(totalprice)
            totalprice = str(totalprice) + "万"
            data.append(totalprice)


            findaverageprice = r'(\d+)元/㎡'
            averageprice = re.search(findaverageprice, item).group(1)
            data.append(averageprice)
            averageprice = str(averageprice) + "元/㎡"
            data.append(averageprice)

            datalist.append(data)
        time.sleep(60)
    return datalist


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, dbpath):
    if not os.path.exists(dbpath):
        print("Database does not exist. Creating a new one...")
        init_db(dbpath)
    else:
        print("Database exists. Updating data...")

    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()


    cur.execute("DELETE FROM price")
    conn.commit()

    for data in datalist:
        for index in range(len(data)):
            if index == 2 or index == 4:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            INSERT INTO price (
                area, name, totalpricevalue, totalprice, averagepricevalue, averageprice
            ) VALUES (%s)
        ''' % ",".join(data)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        CREATE TABLE IF NOT EXISTS price (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area VARCHAR,
            name VARCHAR,
            totalpricevalue NUMERIC,
            totalprice VARCHAR,
            averagepricevalue INTEGER,
            averageprice VARCHAR
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
