from Savoir import Savoir
rpcuser = 'multichainrpc'
rpcpasswd = '489uBCm1zqQQb8P9Thh5kLc5K3j5ZegvW67u1ZD67e2n'
rpchost = 'localhost'
rpcport = '6460'
chainname = 'chain1'

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
print(api.getinfo())
