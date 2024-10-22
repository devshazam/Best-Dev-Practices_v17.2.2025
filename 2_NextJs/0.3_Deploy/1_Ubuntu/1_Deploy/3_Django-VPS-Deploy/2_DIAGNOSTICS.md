nginx
    sudo cat /var/log/nginx/error.log // вывести журнал ошибок
    sudo nginx -t // проверка на синтаксические ибки
    sudo systemctl status nginx // работает ли сервер
    sudo systemctl restart nginx

systemctl
    journalctl -u telebot7.kopi34.ru.gunicorn.service
    sudo systemctl restart telebot7.kopi34.ru.gunicorn.service
    sudo systemctl daemon-reload

    sudo systemctl status <your>.service 

ufw
    watch tail -n 15 /var/log/auth.log

MongoDB
    sudo cat /var/log/mongodb/mongod.log



- pm2
    - info: 
        - pm2 не перезагрузает приложение по умолчанию при изменении файлов, для этого нужно добавить (--watch) в конец команды запуска
        - pm2 самостоятельно отлавливает ошибки и записывает их всвой журнал ошибок ($ pm2 log <--lines 40>); 
        - Критические ошибки перезагружают pm2 (это видно в таблице (pm2 list)); 
    - $ pm2 logs <--lines 40> // получить вывод в консоль 40 строк журналов (втч с ошибками) всех приложений
        - pm2 logs <appname> <--lines 40> // журналы одного приложения appname
        - $ pm2 flush // очиститть журналы
    - $ pm2 monit // показывает текущие процессы 
    - $ pm2 list // показывает статические данные 