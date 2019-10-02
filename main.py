# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime
import pymongo

from flask import Flask, render_template
from google.cloud import datastore

import random


app = Flask(__name__)
datastore_client = datastore.Client()
# client = pymongo.MongoClient("mongodb+srv://db_access_user:OurCloset@ourcloset-3thrj.mongodb.net/test?retryWrites=true&w=majority")

def get(username):
    """Gets users by their username"""
    mydb = client['ourcloset']
    mycol = mydb['users']
    user = mycol.find({"user_name": username})
    return user[0]

def get_collections(collection):
    mydb = client['ourcloset']
    mycol = mydb[collection]
    # return all the items from collection
    return mycol.find() 

@app.route('/')
def root():

    # Fetch the most recent user from the Datastore
    # users = get_collections('users')
    users = [
        {"user_name": "Will"},
        {"user_name": "Ron"},
        {"user_name": "David"},
        {"user_name": "Sanika"},
        ]

    return render_template('index.html', users=users)

@app.route('/profile')
def profile_page():
    user_id = "Bruce Wayne"
    return render_template('profile.html', user_id=user_id)

@app.route('/closet')
def closet_page():
    user_id = "Tony Stark"
    return render_template('closet.html', user_id=user_id)

@app.route('/item')
def item_page():
    user_id = "Kylo Ren"
    return render_template('item.html', user_id=user_id)

@app.route('/items')
def items_page():
    user_id = "Steve Rogers"
    return render_template('items.html', user_id=user_id)
    

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
