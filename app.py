from flask import Flask, render_template, request
from Savoir import Savoir
from creds import *
# RPC call wrappers simplified and abstracted through savoir
# which are located in creds.py
rpchost = 'localhost'
rpcport = '736'
chainname = 'chain1'
api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

infoabc = apiabc.getinfo()
infocorp1 = apicorp1.getinfo()
infocorp2 = apicorp2.getinfo()
infocorp3 = apicorp3.getinfo()
infocorp4 = apicorp4.getinfo()
infocorp5 = apicorp5.getinfo()
infocorp6 = apicorp6.getinfo()
infocorp7 = apicorp7.getinfo()
infocorp8 = apicorp8.getinfo()
infocorp9 = apicorp9.getinfo()

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('index.html',
    info1 = str(infoabc),
    info2 = str(infoabc['chainname']))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/echo", methods=['POST'])
def echo(): 
    return "You said: " + request.form['text']

@app.route('/testhome')
def testhome():
    return render_template('testhome.html')

@app.route("/submit")
def submitTransaction():

    return render_template('submit.html')

@app.route("/")
def hello():

    return '''
    
<html>
    <head>
        <title>CUTC - Deloitte</title>
    </head>
    <body>
        <div class="chain abc">
            <p>Info: ''' + str(infoabc) + '''!</p>
            <h1>chainname: ''' + str(infoabc['chainname']) + '''</h1>
        </div>

        <div class="chain corp1">
            <p>Info: ''' + str(infocorp1) + '''!</p>
            <h1>chainname: ''' + str(infocorp1['chainname']) + '''</h1>
        </div>

        <div class="chain corp2">
            <p>Info: ''' + str(infocorp2) + '''!</p>
            <h1>chainname: ''' + str(infocorp2['chainname']) + '''</h1>
        </div>

        <div class="chain corp3">
            <p>Info: ''' + str(infocorp3) + '''!</p>
            <h1>chainname: ''' + str(infocorp3['chainname']) + '''</h1>
        </div>

        <div class="chain corp4">
            <p>Info: ''' + str(infocorp4) + '''!</p>
            <h1>chainname: ''' + str(infocorp4['chainname']) + '''</h1>
        </div>
        
        <div class="chain corp5">
            <p>Info: ''' + str(infocorp5) + '''!</p>
            <h1>chainname: ''' + str(infocorp5['chainname']) + '''</h1>
        </div>

        <div class="chain corp6">
            <p>Info: ''' + str(infocorp6) + '''!</p>
            <h1>chainname: ''' + str(infocorp6['chainname']) + '''</h1>
        </div>

        <div class="chain corp7">
            <p>Info: ''' + str(infocorp7) + '''!</p>
            <h1>chainname: ''' + str(infocorp7['chainname']) + '''</h1>
        </div>

        <div class="chain corp8">
            <p>Info: ''' + str(infocorp8) + '''!</p>
            <h1>chainname: ''' + str(infocorp8['chainname']) + '''</h1>
        </div>

        <div class="chain corp9">
            <p>Info: ''' + str(infocorp9) + '''!</p>
            <h1>chainname: ''' + str(infocorp9['chainname']) + '''</h1>
        </div>
    </body>
</html>'''