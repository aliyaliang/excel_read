"""pip install dwebsocket==0.5.11"""
import json
from websocket import create_connection

#http/https ws/wss ssl
url = "ws://49.235.92.12:7005/test_websocket"

while True:
    ws = create_connection(url)
    s = input("输入请求内容：")
    ws.send(s)
    response = ws.recv()
    print(response)
    print(json.loads(response)["server_msg"])
