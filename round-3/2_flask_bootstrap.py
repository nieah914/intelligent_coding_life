from flask import Flask, render_template , request
from sql.sql_tools import QueryManager
import json
import asyncio
from flask_restx import Resource, Api
from model.codeMaster import CodeMaster
from model.main import Main
from model.popup.mamul import POPUP_MAMUL

# static 추가
app = Flask(__name__, static_folder='./static/')
api = Api(app)

api.add_namespace(CodeMaster, '/admin/codeMaster')
api.add_namespace(Main, '/')
api.add_namespace(POPUP_MAMUL, '/mamul_desc')


@app.route('/juja')
def view_juja():
    return render_template('index.html')


@app.route('/juja2')
def view_juja2():
    return render_template('widgets.html')

@app.route('/default3')
def view_default3():
    return render_template('view03.html')

@app.route('/default2')
def view_default2():
    return render_template('view02.html')

@app.route('/main')
def main():
    return render_template('view01.html')

@app.route('/test')
def test23():
    return render_template('test.html')
@app.route('/login')
def login():
    return render_template('auth_login.html')


@app.route('/mamul_desc')
def popup_mamul():
    return render_template('popup_mamul_detail.html')


@app.route('/default')
def view_default():
    return render_template('view01.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port='8087')