from flask import Flask
from Savoir import Savoir



app = Flask(__name__)

@app.route("/")
def hello():
    rpcuser = 'multichainrpc'
    rpcpasswd = 'CTf7sJBaxzQbNB3gWBUqE3VRD4xKYNirjeTLSVk6LWej'
    rpchost = 'localhost'
    rpcport = '6460'
    chainname = 'chain1'
    api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
    return "Hello World!" + api.getinfo()
    