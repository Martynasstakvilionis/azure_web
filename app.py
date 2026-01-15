import flask
from flask import Flask, jsonify, request, abort, make_response, url_for, redirect, render_template, flash



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)