import websocket as ws
import json

from websocket import WebSocketConnectionClosedException, WebSocketTimeoutException

websocket = None
try:
    websocket = ws.create_connection(
        url='wss://ws.tst.sora2.soramitsu.co.jp', #node endpoint
        timeout=20, #timeout in seconds
        max_size=2 ** 32,
        read_limit=2 ** 32,
        write_limit=2 ** 32,
    )
except (Exception, WebSocketTimeoutException, WebSocketConnectionClosedException):
    print(408)
    exit(0)

payload = {
    "jsonrpc": "2.0",
    "method": "system_syncState",
    "params": [],
    "id": 1
}
result = {}
try:
    websocket.send(json.dumps(payload))
    result = json.loads(websocket.recv())
except WebSocketConnectionClosedException:
    print(408)
    exit(0)

block_diff = result['result']['highestBlock'] - result['result']['currentBlock']
if block_diff >= 10:
    print(409)
else:
    print(200)

