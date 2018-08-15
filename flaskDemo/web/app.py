# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def post_json_handler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return jsonify('JSON posted')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
