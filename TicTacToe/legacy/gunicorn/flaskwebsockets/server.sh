uwsgi --master --socket 0.0.0.0:5008 --wsgi server:app --buffer-size=32768
