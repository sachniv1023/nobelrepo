#!/usr/bin/env python

#import necessary libraries
# pip install flask 
#export FLASK_APP=flask-app
#flask run
from flask import Flask, json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)
#decorator 
@app.route("/")
def echo_hello():
    return "<p>Hello nobel prize homepage!</p>"


@app.route("/all")
def all():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    #render_template is always looking in templates folder
    return render_template('index.html',data=data_json)


@app.route("/<year>", methods = ["GET"])
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']
    output_data = [x for x in data if x['year']==year]
    #render_template is always looking in templates folder
    return render_template('index.html',data=output_data)

    
if __name__ == "__main__":
    app.run(debug=True)
