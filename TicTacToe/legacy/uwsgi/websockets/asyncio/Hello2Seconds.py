import asyncio

def two_seconds_elapsed():
    print("Hello 2 seconds elapsed")

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    asyncio.get_event_loop().call_later(2, two_seconds_elapsed)
    return [b"Hello World 12345"]
