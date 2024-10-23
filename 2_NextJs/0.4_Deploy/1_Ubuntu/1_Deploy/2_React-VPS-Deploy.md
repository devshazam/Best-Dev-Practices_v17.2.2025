Ссылка на основной гайд: https://www.youtube.com/watch?v=Qu-oyzWIpjI&list=WL&index=3&t=1184s
1) Развернуть VPS сервер Ubuntu 22.04
2) Установить:
    - Git
    - sudo apt update
    - sudo install nodejs 
    - sudo install npm
    - sudo npm install pm2 -g
    - sudo apt install nginx
3) Деплой проекта
    - git config --global credential.helper store // сохранение паролей
    - git clone ...
5) Перенаправление домена на IP
    - Заменить А-запись домена на - IP // ping домен (проверка IP)
    - Конфигурационные фйлы сервера nginx 
        - sudo nano /etc/nginx/sites-available/default 
            - server {
                        listen 80;
                        listen [::]:80;
                        root /var/www/html;
                        index index.html index.htm index.nginx-debian.html;
                        server_name доменное_имя;
                        location / {
                                proxy_pass http://localhost:ваш_порт;
                                proxy_http_version 1.1;
                                proxy_set_header Upgrade $http_upgrade;
                                proxy_set_header Connection 'upgrade';
                                proxy_set_header Host $host;
                                proxy_cache_bypass $http_upgrade;
                        }
                }
            - sudo nginx -t // ошибки синтаксиса
            - sudo service nginx restart // Перезагрузка nginx для применения изменений
            - `sudo ln -s /etc/nginx/sites-available/название_вашего_конфига /etc/nginx/sites-enabled/` // создание ссылки 
    - Конфигурация файла /etc/nginx/nginx.conf // разрешение загружать файлы более 1 Мб
6) Установка ssl сертификаатов - https://beget.com/ru/kb/how-to/vps/vypusk-i-ustanovka-ssl-sertifikatov-ot-lets-encrypt-na-vps
        
