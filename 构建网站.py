from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def mian():  # put application's code here
    return render_template('mian.html')
@app.route('/main1')
def mian1():  # put application's code here
    return render_template('mian1.html')
@app.route('/dapengxinqv1')
def dapengxinqv1():  # put application's code here
    return render_template('dapengxinqv1.html')
@app.route('/pingshan1')
def pingshan1():  # put application's code here
    return render_template('pingshan1.html')
@app.route('/nanshan1')
def nanshan1():  # put application's code here
    return render_template('nanshan1.html')
@app.route('/luohu1')
def luohu1():  # put application's code here
    return render_template('luohu1.html')
@app.route('/longhua1')
def longhua1():  # put application's code here
    return render_template('longhua1.html')
@app.route('/longgang1')
def longgang1():  # put application's code here
    return render_template('longgang1.html')
@app.route('/futian1')
def futian1():  # put application's code here
    return render_template('futian1.html')
@app.route('/yantian1')
def yantian1():  # put application's code here
    return render_template('yantian1.html')
@app.route('/baoan1')
def baoan1():  # put application's code here
    return render_template('baoan1.html')
@app.route('/guangming1')
def guangming1():  # put application's code here
    return render_template('guangming1.html')
@app.route('/nanshan')
def nanshan():
    i=0
    datalist=[]
    con = sqlite3.connect("price.db")
    cur=con.cursor()
    sql="select * from price"
    data=cur.execute(sql)
    for item in data:
        if item[1]=='坪山':
            break
        item = list(item)
        i += 1
        item.append(i)
        item = tuple(item)
        datalist.append(item)


    cur.close()
    con.close()
    return render_template('nanshan.html',nanshandata=datalist)

@app.route('/pingshan')
def pingshan():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1]=='坪山':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '龙岗':
            break
    cur.close()
    con.close()


    return render_template('pingshan.html', nanshandata=datalist)
@app.route('/longgang')
def longgang():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1]== '龙岗':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '宝安':
            break
    cur.close()
    con.close()

    return render_template('longgang.html', nanshandata=datalist)

@app.route('/baoan')
def baoan():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '宝安':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '龙华':
            break
    cur.close()
    con.close()

    return render_template('baoan.html', nanshandata=datalist)

@app.route('/longhua')
def longhua():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '龙华':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '福田':
            break
    cur.close()
    con.close()

    return render_template('longhua.html', nanshandata=datalist)

@app.route('/futian')
def futian():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '福田':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '罗湖':
            break
    cur.close()
    con.close()

    return render_template('futian.html', nanshandata=datalist)

@app.route('/luohu')
def luohu():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '罗湖':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '光明':
            break
    cur.close()
    con.close()

    return render_template('luohu.html', nanshandata=datalist)

@app.route('/guangming')
def guangming():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '光明':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '盐田':
            break
    cur.close()
    con.close()

    return render_template('guangming.html', nanshandata=datalist)

@app.route('/yantian')
def yantian():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '盐田':
            item=list(item)
            i += 1
            item.append(i)
            item=tuple(item)
            datalist.append(item)

        if item[1] == '大鹏新区':
            break
    cur.close()
    con.close()

    return render_template('yantian.html', nanshandata=datalist)

@app.route('/dapengxinqv')
def dapengxinqv():
    i = 0
    datalist = []
    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select * from price"
    data = cur.execute(sql)
    for item in data:
        if item[1] == '大鹏新区':
            item = list(item)
            i += 1
            item.append(i)
            item = tuple(item)
            datalist.append(item)

        if item[1] == '':
            break
    cur.close()
    con.close()

    return render_template('dapengxinqv.html', nanshandata=datalist)

@app.route('/total')
def total():
    area=[]
    totalpricevalue=[]
    averagepricevalue=[]

    con = sqlite3.connect("price.db")
    cur = con.cursor()
    sql = "select area,avg(totalpricevalue),avg(averagepricevalue) from price group by area"
    data = cur.execute(sql)
    for item in data:
        area.append(str(item[0]))
        totalpricevalue.append(int(item[1]*10))
        averagepricevalue.append(int(item[2]))
    cur.close()
    con.close()
    # put application's code here
    return render_template('total.html',area=area,totalpricevalue=totalpricevalue,averagepricevalue=averagepricevalue)
if __name__ == '__main__':
    app.run()
