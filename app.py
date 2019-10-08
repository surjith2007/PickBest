import warnings
from flask import (Flask, session, g, json, Blueprint, flash, jsonify, redirect, render_template, request,
                   url_for, send_from_directory)
import search

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

app = Flask(__name__)

app.config.from_object(__name__)  # load config from this file , flaskr.py

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf','.doc'])


@app.route('/')
def home():
    x = []
    return render_template('index.html', results=x)

@app.route('/search', methods=['POST', 'GET'])
def resultsearch():
    if request.method == 'POST':
        search_st = request.form.get('Name')
        print(search_st)
    result = search.res(search_st)
    # return result
    return render_template('result.html', results=result)


if __name__ == '__main__':
    # app.run(debug = True)
    # app.run('127.0.0.1' , 5000 , debug=True)
    app.run('0.0.0.0', 5000, debug=True, threaded=True)

