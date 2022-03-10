ШАГИ установки:

1) В открытом терминале создать дирректорию, в которой планируется располагать файлы и заходим в нее

2) выполняем команду, копируя содержимое проекта:

      git clone https://github.com/ZverevDmitriyZDV/Terminal-HW2.git

3) Проходим в дирректорию simple_crud b создаем докер:
      docker build --tag=hw2ed1 .

4) запуск c указанием переменных окружений DEBUG SEKRET_KEY
      docker run -e DEBUG=True -e SECRET_KEY='the-best-secret-key' --name=hw2_server_main -d -p 8000:80 hw2ed1:latest
      
     -e DEBUG=True -e SECRET_KEY='the-best-secret-key' - возможно менять

5) проверка корректного запуска:
       docker logs hw2_server_main