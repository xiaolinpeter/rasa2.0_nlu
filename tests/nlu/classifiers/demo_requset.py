# -*- coding: utf-8 -*-
'''
@time: 2020/11/30 下午4:51
@author: xiaolin_peter
@contact: xiaolin_peter@163.com
@File demo_requset.py
'''
from flask import (Flask, request)
from rasa.nlu.components import ComponentBuilder
from rasa.nlu.model import Interpreter

component_builder = ComponentBuilder()
model_path1 = "/Users/xiaolin_peter/virtual_environment/rasa2.0_nlu/tests/nlu/models/"
import json

app = Flask(__name__)


@app.route('/message', methods=['GET', 'POST'])
def rasa_result():
    comment = request.get_data()
    json_data = json.loads(comment.decode())
    text = json_data["q"]
    model_path = model_path1 + json_data["model"]
    loaded = Interpreter.load(model_path, component_builder)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    return loaded.parse(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, debug=True)
