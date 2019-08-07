
### Mummy Money

* Create your admin user
```
python manage.py createsuperuser
```

* Deploy database
```
python makemigrations
python manage.py migrate --run-syncdb
```