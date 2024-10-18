RUN:
    $ docker run <options> <container_name>
    $ docker run --name my_nginx -p 3202:3000 -it -v ${pwd}:/usr/share/nginx/html <container_name>
        $ --name my_nginx - задать собственное имя контейнера
        $ -p 8080:80 - публичный порт 8080 - внутренний порт 80
        $ -it // интерактивный терминал
        $ -v ${pwd}:/usr/share/nginx/html - замена тома
        $ -d // запуск в фоновом режиме
        $ --rm - удаляет контейнеры после остановки

Dockerfile:
    $ docker build -t name:teg . // построить образ из dockerfile в текущей папке
          $ -t name:teg // испольховать свои имя и тег (можжно без тега)
          $ -f dockerfile.dev // использовать данный файл для сборки

Docker_Compose:
    $ docker compose up # Execute (similar with docker run -it)
    $ docker compose up -d 