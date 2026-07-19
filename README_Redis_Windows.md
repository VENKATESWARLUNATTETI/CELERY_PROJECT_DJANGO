# Redis on Windows (Docker & WSL) Cheat Sheet

## Option 1: Run Redis with Docker (Recommended)

### Pull and Run Redis

``` bash
docker run -d --name redis -p 6379:6379 redis
```

### Check Running Containers

``` bash
docker ps
```

### Check All Containers

``` bash
docker ps -a
```

### Start Redis Container

``` bash
docker start redis
```

### Stop Redis Container

``` bash
docker stop redis
```

### Restart Redis Container

``` bash
docker restart redis
```

### Remove Redis Container

``` bash
docker rm redis
```

### Remove Forcefully

``` bash
docker rm -f redis
```

### View Redis Logs

``` bash
docker logs redis
```

### Open Redis CLI

``` bash
docker exec -it redis redis-cli
```

### Test Redis

``` text
PING
PONG
```

### Exit Redis CLI

``` text
exit
```

------------------------------------------------------------------------

# Option 2: Run Redis using WSL (Ubuntu)

## Install Redis

``` bash
sudo apt update
sudo apt install redis-server
```

## Start Redis

``` bash
sudo service redis-server start
```

## Stop Redis

``` bash
sudo service redis-server stop
```

## Restart Redis

``` bash
sudo service redis-server restart
```

## Check Redis Status

``` bash
sudo service redis-server status
```

## Test Redis

``` bash
redis-cli ping
```

Expected output:

``` text
PONG
```

## Open Redis CLI

``` bash
redis-cli
```

## Exit Redis CLI

``` text
exit
```

------------------------------------------------------------------------

# Verify Redis Port

``` bash
netstat -ano | findstr 6379
```

------------------------------------------------------------------------

# Django / Celery Configuration

``` python
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
```

Run Django:

``` bash
python manage.py runserver
```

Run Celery Worker:

``` bash
celery -A <project_name> worker --pool=solo -l info
```

Replace `<project_name>` with your Django project name.

------------------------------------------------------------------------

# Quick Commands

## Docker

  Task        Command
  ----------- -------------------------------------------------
  Run Redis   `docker run -d --name redis -p 6379:6379 redis`
  Start       `docker start redis`
  Stop        `docker stop redis`
  Restart     `docker restart redis`
  Status      `docker ps`
  CLI         `docker exec -it redis redis-cli`
  Remove      `docker rm -f redis`

## WSL

  Task      Command
  --------- -------------------------------------
  Install   `sudo apt install redis-server`
  Start     `sudo service redis-server start`
  Stop      `sudo service redis-server stop`
  Restart   `sudo service redis-server restart`
  Status    `sudo service redis-server status`
  Test      `redis-cli ping`
