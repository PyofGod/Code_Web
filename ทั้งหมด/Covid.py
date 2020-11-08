import urllib, json, requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    # ระบุเเป้าหมายข้อมูล json และ API
    api = requests.get("https://covid19.th-stat.com/api/open/today")

    # ดึงข้อมูล
    data = {
    'confirmed': str(api.json()['Confirmed']),
    'recovered': str(api.json()['Recovered']),
    'hospitalized': str(api.json()['Hospitalized']),
    'death': str(api.json()['Deaths'])
    }
    # แสดงโค้ด
    print(data)
    # แสดงข้อข้อมูลผ่าน covid19.html และใช้ข้อมูลของ DATA
    return render_template('covid.html', data = data)
    #str(response.json()['Confirmed'])
if __name__ == "__main__":
    app.run( debug=True)


    