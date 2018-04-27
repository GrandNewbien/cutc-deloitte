from Savoir import Savoir
rpcuser = 'multichainrpc'
rpcpasswd = 'CTf7sJBaxzQbNB3gWBUqE3VRD4xKYNirjeTLSVk6LWej'
rpchost = 'localhost'
rpcport = '6460'
chainname = 'chain1'

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
print(api.getinfo())
