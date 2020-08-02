import time
from pygate_grpc.client import PowerGateClient
from google.protobuf.json_format import MessageToDict


client = PowerGateClient("127.0.0.1:5002")

wallets = client.wallet.list()
print("Wallets:")
print(wallets)


print("Creating a new FFS:")
newFfs = client.ffs.create()
print(newFfs)

addresses = client.ffs.addrs_list(newFfs.token)
wallt = addresses.addrs[0].addr
print("FFS wallet: " + wallt)

print("Waiting for wallet to get funding...")
time.sleep(2)

balance = client.wallet.balance(wallt)
print("Wallet balance: ", str(balance.balance))
