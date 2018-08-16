# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def post_json_handler():
    print (request.is_json)
    content = request.get_json()
    print (content)

    ret = parse_json(content)
    return ret

def parse_json(json_data):
    ret = {}
    
    for key, value in json_data.items():
        if type(value) is int:
            ret[key] = value * 100
        elif type(value) is str:
            ret[key] = value + " is cool!"

    return json.dumps(ret)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
