import socketio

# standard Python
sio = socketio.Client()

# asyncio
## sio = socketio.AsyncClient()

@sio.event
def message(data):
    print('I received a message!')

@sio.on('my message')
def on_message(data):
    print('I received a message!')

##@sio.event
##async def message(data):
##    print('I received a message!')

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")
   
sio.connect('http://localhost:5002')

## await sio.connect('http://localhost:5002')

print('my sid is', sio.sid)

sio.emit('my message', {'foo': 'bar'})

