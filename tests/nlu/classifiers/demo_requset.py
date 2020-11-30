# -*- coding: utf-8 -*-
'''
@time: 2020/11/30 下午4:51
@author: xiaolin_peter
@contact: xiaolin_peter@163.com
@File demo_requset.py
'''
from flask import jsonify
from flask import (Flask, render_template, request)
from rasa.nlu.components import ComponentBuilder
from rasa.nlu.classifiers.diet_classifier import DIETClassifier
from rasa.nlu.model import Interpreter
component_builder = ComponentBuilder()
import json
app = Flask(__name__)
@app.route('/message', methods=['GET', 'POST'])
def rasa_result():
    loaded = Interpreter.load('/Users/xiaolin_peter/virtual_environment/rasa-master/tests/nlu/models/nlu_20201130-203700', component_builder)
    assert loaded.pipeline
    comment = request.get_data()
    json_data = json.loads(comment.decode())
    print("用户请求=======", json_data)
    text = json_data["question"]
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    return loaded.parse(text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, debug=True)


