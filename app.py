from flask import Flask, render_template, redirect, url_for, request, session, Response
from functools import wraps
import pymongo

import pandas as pd
import numpy as np
import logging
import datetime
import os.path
from flask import Markup
import os

import mediapipe as mp

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


# Routes
from user import routes


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':

    app.run()