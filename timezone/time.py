from flask import Flask, render_template, request
import requests
import json
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class NameForm(FlaskForm):
    citys =StringField("citys")
    submit = SubmitField('提交')

app = Flask(__name__)

app.config["SECRET_KEY"] = "fdsafdafad"


@app.route('/')
def student():
    return render_template('time.html')


@app.route('/result', methods = ['GET', 'POST'])
def result():
    form = NameForm()
    if request.method == 'POST':
        citys = form.citys.data
        url = 'http://api.tianapi.com/txapi/worldtime/index'
        body = {
            "key": " ",   #需要自己去申请
            "city": citys}
        headers = {'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(url, data=body, headers=headers)
        js = json.loads(response.text)
        if js["code"] == 200:
            timezone = js["newslist"][0]['timeZone']
            time1 = js["newslist"][0]['strtime']
            return render_template("result.html", result=result, form=form, citys=citys, timezone=timezone, time1=time1)
        else:
            return render_template("error.html", result=result)


if __name__ == '__main__':
    app.run(debug = True)

