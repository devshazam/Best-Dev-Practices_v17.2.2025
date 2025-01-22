# Установка
  	$ sudo npm install -g pm2

# Конфигурация
	$ pm2 startup // Запускать автоматически при запуске или перезапуске системы
	$ pm2 save
	$ pm2 start index.js --name <appname> --time --watch // запуск под именем
		--time // для вставки времени в логи ошибок 
		--name <name> // для именования 
		--watch // перезагружать приложение при изменении файлов !!! я делфю в ручную
	$ pm2 start npm --name <app-name> --time -- start // запуски приложения через npm

# Работа с ошибками
	$ pm2 logs <appname> --lines 40 // журналы appname приложения по 40 строк
	$ pm2 flush - очиститть журналы



