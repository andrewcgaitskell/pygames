https://github.com/heroku-python/flask-sockets

run it

gunicorn -k flask_sockets.worker hello:app
