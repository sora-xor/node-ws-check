import websocket as websocket
import json

websocket = websocket.create_connection(
    url='wss://ws.tst.sora2.soramitsu.co.jp', #node endpoint
    timeout=20,
    max_size=2 ** 32,
    read_limit=2 ** 32,
    write_limit=2 ** 32,
)

payload = {
    "jsonrpc": "2.0",
    "method": "system_chain",
    "params": [],
    "id": 1
}

websocket.send(json.dumps(payload))

result = json.loads(websocket.recv())
print(result['result'])


