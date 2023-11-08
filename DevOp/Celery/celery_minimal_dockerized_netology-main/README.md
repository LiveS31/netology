
### 1. Запускаем redis 

```shell
docker-compose --env-file .env.test up redis
```

в выводе должна присутсвовать строка 

```
celery_minimal_dockerized_netology-redis-1  | ............ * Ready to accept connections
```

### 2. Запускаем celery

в другой вкладке терминала запускаем celery 

```shell
docker-compose --env-file .env.test up celery
```

должен получится вывод без ошибок  наподобие такого:

```
celery_minimal_dockerized_netology-celery-1  |  -------------- celery@e763174649e8 v5.2.7 (dawn-chorus)
celery_minimal_dockerized_netology-celery-1  | --- ***** ----- 
celery_minimal_dockerized_netology-celery-1  | -- ******* ---- Linux-5.4.0-135-generic-x86_64-with-glibc2.31 2022-12-26 07:03:39
celery_minimal_dockerized_netology-celery-1  | - *** --- * --- 
celery_minimal_dockerized_netology-celery-1  | - ** ---------- [config]
celery_minimal_dockerized_netology-celery-1  | - ** ---------- .> app:         __main__:0x7f41504f5ab0
celery_minimal_dockerized_netology-celery-1  | - ** ---------- .> transport:   redis://db-redis:6379/1
celery_minimal_dockerized_netology-celery-1  | - ** ---------- .> results:     redis://db-redis:6379/2
celery_minimal_dockerized_netology-celery-1  | - *** --- * --- .> concurrency: 12 (prefork)
celery_minimal_dockerized_netology-celery-1  | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
celery_minimal_dockerized_netology-celery-1  | --- ***** ----- 
celery_minimal_dockerized_netology-celery-1  |  -------------- [queues]
celery_minimal_dockerized_netology-celery-1  |                 .> celery           exchange=celery(direct) key=celery
```

### 3. Запускаем приложение
в другой вкладке терминала запускаем приложение

```shell
docker-compose --env-file .env.test up app
```

В выводе должны получить:
```
celery_minimal_dockerized_netology-app-1  | Hello World
celery_minimal_dockerized_netology-app-1  | Hello World
celery_minimal_dockerized_netology-app-1  | Hello World
celery_minimal_dockerized_netology-app-1  | Hello World
celery_minimal_dockerized_netology-app-1 exited with code 0

```
