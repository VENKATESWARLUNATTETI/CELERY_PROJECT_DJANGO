# Redis Commands Cheat Sheet (Linux)

## Install

``` bash
sudo apt update
sudo apt install redis-server -y
```

## Start Redis

``` bash
sudo systemctl start redis
sudo systemctl start redis-server
sudo service redis start
sudo service redis-server start
redis-server
```

## Run in Background

``` bash
redis-server --daemonize yes
```

## Check Status

``` bash
sudo systemctl status redis
sudo service redis status
```

## Restart

``` bash
sudo systemctl restart redis
sudo service redis restart
```

## Reload

``` bash
sudo systemctl reload redis
```

## Stop Redis

``` bash
sudo systemctl stop redis
sudo service redis stop
redis-cli shutdown
```

## Enable / Disable Auto Start

``` bash
sudo systemctl enable redis
sudo systemctl disable redis
```

## Check Process

``` bash
ps -ef | grep redis
pgrep redis-server
pidof redis-server
```

## Connect to Redis

``` bash
redis-cli
```

## Test Connection

``` bash
redis-cli ping
```

## Check Version

``` bash
redis-server --version
redis-cli --version
```

## Check Port

``` bash
ss -tlnp | grep 6379
netstat -tlnp | grep 6379
```

## View Logs

``` bash
sudo journalctl -u redis
```

## Common Redis CLI Commands

``` text
PING
SET key value
GET key
DEL key
KEYS *
EXISTS key
INFO
DBSIZE
FLUSHDB
FLUSHALL
QUIT
```

## Kill Redis Process

``` bash
kill <PID>
kill -9 <PID>
```
