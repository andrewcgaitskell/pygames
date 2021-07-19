#!/usr/bin/env python

# WS server example

import asyncio
import websockets
from datetime import datetime

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"Raspi< {name}")

    greeting = f"Raspi says Hello {name}!"

    await websocket.send(greeting)
    print(f"Raspi> {greeting}")

# host = "<explicit IP>" works 
# Also host="" seems to work for external access
# start_server = websockets.serve(hello, host="10.0.2.29", port=8765)
#start_server = websockets.serve(hello, host="" , port=5010)
start_server = websockets.serve(hello, host="127.0.0.1", port=5011)

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_server)
        loop.run_forever()
    except:
        print(f"All Over")
