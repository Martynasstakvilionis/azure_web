import os, sys, json, datetime, re, random, string, shutil, threading
from flask import Flask, jsonify, request, abort, make_response, url_for, redirect, render_template, flash


app = Flask(__name__)


@app.route('/')
def index():
    fredag = datetime.datetime.now().weekday() == 4
    if fredag: 
        if_fredag = "Ja"
    else: 
        if_fredag = "Nei"
        

    return render_template('index.html', if_fredag=if_fredag)



if __name__ == '__main__':
    app.run(debug=True)