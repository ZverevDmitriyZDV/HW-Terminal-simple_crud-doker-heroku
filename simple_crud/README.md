# ШАГИ установки:

1) В открытом терминале создать дирректорию, в которой планируется располагать файлы и заходим в нее выполняем команду, копируя содержимое проекта:
```shell
    git clone https://github.com/ZverevDmitriyZDV/Terminal-HW2.git
```
2) проходим в дирректорию simple_crud и создаем докер 
```shell
    docker build --tag=hw2ed1 .
```
3) запуск c указанием переменных окружений `DEBUG` и `SEKRET_KEY`
```shell
    docker run -e DEBUG=True -e SECRET_KEY='the-best-secret-key' --name=hw2_server_main -d -p 8000:8000 hw2ed1:latest
```
`-e DEBUG=True`, `-e SECRET_KEY='the-best-secret-key'` - возможно менять
4) проверка корректного запуска
```shell
    docker logs hw2_server_main
```

5) проверка корректного запуска:
```shell
    docker logs hw2_server_main
```

6) остановка docker:
```shell
   docker stop hw2_server_main

```
       