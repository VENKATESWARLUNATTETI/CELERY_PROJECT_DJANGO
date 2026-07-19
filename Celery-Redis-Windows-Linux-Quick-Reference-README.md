# Celery + Redis (Windows/Linux) Quick Reference

## 1. Activate Virtual Environment

### Windows

``` powershell
.venv\Scripts\activate
```

### Linux/macOS

``` bash
source .venv/bin/activate
```

------------------------------------------------------------------------

## 2. Start Redis

### Docker

``` bash
docker run -d --name redis -p 6379:6379 redis
```

### Check running containers

``` bash
docker ps
```

### Stop Redis

``` bash
docker stop redis
```

### Start existing container

``` bash
docker start redis
```

### Restart Redis

``` bash
docker restart redis
```

### Remove container

``` bash
docker rm -f redis
```

------------------------------------------------------------------------

## 3. Linux Native Redis

Start:

``` bash
redis-server
```

Background:

``` bash
redis-server --daemonize yes
```

Stop:

``` bash
redis-cli shutdown
```

Ping:

``` bash
redis-cli ping
```

Expected:

``` text
PONG
```

------------------------------------------------------------------------

## 4. Celery Worker

### Windows (Recommended)

``` bash
python -m celery -A celery_project worker -l info -P solo
```

### Windows (Threads)

``` bash
python -m celery -A celery_project worker -l info -P threads
```

### Linux

``` bash
python -m celery -A celery_project worker -l info
```

------------------------------------------------------------------------

## 5. Django Server

``` bash
python manage.py runserver
```

------------------------------------------------------------------------

## 6. Migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

------------------------------------------------------------------------

## 7. Create Superuser

``` bash
python manage.py createsuperuser
```

------------------------------------------------------------------------

## 8. Test Redis Connection

``` bash
redis-cli ping
```

------------------------------------------------------------------------

## 9. Git Commands

Configure username:

``` bash
git config --global user.name "Your Name"
```

Configure email:

``` bash
git config --global user.email "you@example.com"
```

Check config:

``` bash
git config --global --list
```

------------------------------------------------------------------------

## 10. Docker Commands

``` bash
docker ps
docker ps -a
docker images
docker stop redis
docker start redis
docker restart redis
docker rm redis
docker rm -f redis
docker logs redis
```

------------------------------------------------------------------------

## 11. Common Celery Error

### Error

``` text
PermissionError
WinError 5
WinError 6
```

### Cause

Windows does not fully support the default `prefork` worker pool.

### Fix

``` bash
python -m celery -A celery_project worker -l info -P solo
```

or

``` bash
python -m celery -A celery_project worker -l info -P threads
```

------------------------------------------------------------------------

## 12. Stop Processes

Stop Django/Celery:

``` text
Ctrl + C
```

Stop Docker Redis:

``` bash
docker stop redis
```

Stop Linux Redis:

``` bash
redis-cli shutdown
```

------------------------------------------------------------------------

# Project Startup Order

1.  Activate virtual environment
2.  Start Redis
3.  Start Django server
4.  Start Celery worker (`-P solo` on Windows)
5.  Run your tasks

------------------------------------------------------------------------

## Happy Coding! 🚀
