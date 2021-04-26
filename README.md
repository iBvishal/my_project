# how to run the project

```
1. clone the git repository
2. pipenv shell
```
```
3. pip install -r requirements.txt
```
```
4. cd YoutubeRestAPI/
5. python manage.py runserver
```

```
To Install redis-server run
6. sudo apt install redis-server
```

```
To run celery worker and celery beat
6. celery -A YoutubeRestAPI beat -l INFO
7. celery -A YoutubeRestAPI worker -l INFO
```

Test
After running the project, to test just make following requests
curl http://127.0.0.1:8000/youtubevideometa/?title="titleYouWantToSearch"&description="DescYouAreLookingFor"

todo:
1. Containerize the project