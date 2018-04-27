from flask import Flask
from Savoir import Savoir
#RPC settings to login to a chain
rpcuser = 'multichainrpc'
rpcpasswd = 'CTf7sJBaxzQbNB3gWBUqE3VRD4xKYNirjeTLSVk6LWej'
rpchost = 'localhost'
rpcport = '6460'
chainname = 'chain1'
api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

info = api.getinfo()

app = Flask(__name__)

@app.route("/")
def hello():

    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <p>Info: ''' + str(info) + '''!</p>
        <h1>chainname: ''' + str(info['chainname']) + '''</h1>
    </body>
</html>'''