from flask import Flask, request, jsonify
import json, codecs
import numpy as np
import pandas as pd

app = Flask(__name__)

# Flask Routes
@app.route('/postjson', methods=['POST'])
def post_json_handler():
    data = request.get_json()
    return parse_types(data)

@app.route('/numpy', methods=['POST'])
def create_numpy():
    data = request.get_json()
    return parse_numpy(data)

# Processing
def parse_numpy(data):
    mylist = []
    for row in data:
        mylist.append(row)
    df = pd.DataFrame(mylist)
    df[0] = pd.to_datetime(df[0])
    return df.to_json(orient='values')

def parse_types(data):
    ret = {}
    
    # parse each key/value pair from the JSON data
    for key, value in data.items():
        if type(value) is int:
            ret[key] = value * 100
        elif type(value) is str:
            ret[key] = value + " is cool!"

    return json.dumps(ret)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
