#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"Raspi< {name}")

    greeting = f"Raspi says Hello {name}!"

    await websocket.send(greeting)
    print(f"Raspi> {greeting}")

# host = "<explicit IP>" works 
# Also host="" seems to work for external access
# start_server = websockets.serve(hello, host="10.0.2.29", port=8765)
start_server = websockets.serve(hello, host="" , port=5010)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
