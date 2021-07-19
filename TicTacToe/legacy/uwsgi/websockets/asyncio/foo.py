import asyncio
from datetime import datetime


async def collect_data():
    await asyncio.sleep(1)
    return {"some_data": 1,}


async def foo(loop):
    results = await collect_data()

    # Log the results
    print("{}: {}".format(datetime.now(), results))

    # Schedule to run again in X seconds
    await asyncio.sleep(5)
    return (await foo(loop))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(foo(loop))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())  # Python 3.6 only
        loop.close()
