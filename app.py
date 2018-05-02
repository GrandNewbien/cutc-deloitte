from flask import Flask, render_template, request
from Savoir import Savoir
from creds import *
# RPC call wrappers simplified and abstracted through savoir
# which are located in creds.py

infoabc   = apiabc.getinfo()
infocorp1 = apicorp1.getinfo()
infocorp2 = apicorp2.getinfo()
infocorp3 = apicorp3.getinfo()
infocorp4 = apicorp4.getinfo()
infocorp5 = apicorp5.getinfo()
infocorp6 = apicorp6.getinfo()
infocorp7 = apicorp7.getinfo()
infocorp8 = apicorp8.getinfo()
infocorp9 = apicorp9.getinfo()
abcassets = apiabc.listassets()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html',
    info1 = str(abcassets),
    info2 = str(infoabc['chainname']),
    
    
    
    
    
    )

@app.route("/transact", methods=['POST'])
def echo(): 
    return "You said: " + request.form['text']

