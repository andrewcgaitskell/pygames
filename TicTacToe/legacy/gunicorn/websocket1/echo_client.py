from websocket import create_connection
uri = "ws://player2.acgtest.info:5008/echo"
ws = create_connection(uri)
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
