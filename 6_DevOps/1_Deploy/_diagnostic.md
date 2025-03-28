# Поиск и устранение ошибок в среде Linux
	- nginx
		$ sudo cat /var/log/nginx/error.log // вывести журнал ошибок
		$ sudo nginx -t // проверка на синтаксические ибки
		$ sudo systemctl status nginx // работает ли сервер
		$ sudo systemctl restart nginx

	- pm2
		$ pm2 logs <appname> --lines 40
		$ pm2 flush // очистить журналы
		$ pm2 list // показывает статические данные 

	- ufw
		$ watch tail -n 15 /var/log/auth.log // журнал фаервола
		
	- systemctl
		$ journalctl -u telebot7.kopi34.ru.gunicorn.service // Вывести журналы сервиса
		$ systemctl list-timers // Журнал таймеров - типа крон задач
		$ sudo systemctl restart telebot7.kopi34.ru.gunicorn.service
		$ sudo systemctl daemon-reload
		$ sudo systemctl status telebot7.kopi34.ru.gunicorn.service 

	- Node
		$ ps -e|grep node // поиск node процессов в Linux 

	- CRON
		$ sudo crontab -l // проверить задачи крон списком

	- MongoDB
		$ sudo cat /var/log/mongodb/mongod.log
