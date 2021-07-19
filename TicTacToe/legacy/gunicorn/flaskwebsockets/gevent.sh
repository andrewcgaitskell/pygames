uwsgi --master --socket 0.0.0.0:5008 --buffer-size=32768 --http-websockets --gevent 100 --wsgi server:app
