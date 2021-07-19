#uwsgi --socket 127.0.0.1:5010 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

#uwsgi --http-socket 127.0.0.1:5010 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

# embedded mode
uwsgi --http 127.0.0.1:5010 --wsgi-file foobar.py --master --processes 4 --threads 2

