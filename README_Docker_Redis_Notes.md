# Docker + Redis Notes (Windows)

## 1. Check Docker Installation

``` powershell
docker --version
docker compose version
```

## 2. Verify Docker is Running

``` powershell
docker info
docker ps
```

## 3. Pull the Redis Image

``` powershell
docker pull redis
docker images
```

## 4. Run Redis

``` powershell
docker run -d --name redis -p 6379:6379 redis
```

**Explanation**

-   `-d` → Run in background
-   `--name redis` → Container name
-   `-p 6379:6379` → Map local port to container port

## 5. Check Running Containers

``` powershell
docker ps
```

Check all containers:

``` powershell
docker ps -a
```

## 6. Open Redis CLI

``` powershell
docker exec -it redis redis-cli
```

Test Redis:

``` text
PING
PONG
```

Exit:

``` text
exit
```

## 7. View Logs

``` powershell
docker logs redis
docker logs -f redis
```

## 8. Stop, Start and Restart

``` powershell
docker stop redis
docker start redis
docker restart redis
```

## 9. Remove Container

``` powershell
docker rm redis
docker rm -f redis
```

## 10. Remove Redis Image

``` powershell
docker rmi redis
```

## 11. Inspect Container

``` powershell
docker inspect redis
docker stats
docker stats redis
```

## 12. Open a Shell

``` powershell
docker exec -it redis sh
```

Exit:

``` text
exit
```

## 13. Cleanup

``` powershell
docker container prune
docker image prune
docker image prune -a
docker system prune
docker system prune -a
```

## 14. Stop All Running Containers

**PowerShell**

``` powershell
docker ps -q | ForEach-Object { docker stop $_ }
```

## 15. Check Redis Port

``` powershell
netstat -ano | findstr :6379
```

## Redis Connection URL

``` text
redis://localhost:6379/0
```

or

``` text
redis://127.0.0.1:6379/0
```

## Quick Reference

  Command                                           Purpose
  ------------------------------------------------- ----------------------
  `docker pull redis`                               Download Redis image
  `docker run -d --name redis -p 6379:6379 redis`   Start Redis
  `docker ps`                                       Running containers
  `docker ps -a`                                    All containers
  `docker images`                                   List images
  `docker stop redis`                               Stop container
  `docker start redis`                              Start container
  `docker restart redis`                            Restart container
  `docker exec -it redis redis-cli`                 Redis CLI
  `docker logs redis`                               View logs
  `docker rm redis`                                 Remove container
  `docker rmi redis`                                Remove image
  `docker inspect redis`                            Container details
  `docker stats`                                    Resource usage
  `docker system prune -a`                          Cleanup
