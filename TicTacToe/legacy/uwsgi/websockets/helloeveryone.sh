#uwsgi --http-socket 0.0.0.0:5010 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

uwsgi --http 0.0.0.0:5010 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
