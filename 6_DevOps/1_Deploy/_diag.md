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
		$ watch tail -n 15 /var/log/auth.log
		
	- systemctl
		$ journalctl -u telebot7.kopi34.ru.gunicorn.service
		$ sudo systemctl restart telebot7.kopi34.ru.gunicorn.service
		$ sudo systemctl daemon-reload
		$ sudo systemctl status telebot7.kopi34.ru.gunicorn.service 


	- MongoDB
		$ sudo cat /var/log/mongodb/mongod.log
