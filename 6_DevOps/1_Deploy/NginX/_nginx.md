# 
	- Конфигурационные файлы:
		$ nano /etc/nginx/nginx.conf // общий конфигурационный файл всех настроек nginx 
			- client_max_body_size 100M;
		$ nano /etc/nginx/site-available/default //  
			$ sudo rm /etc/nginx/sites-enabled/default // удалить стартовый файл
		$ nano /etc/nginx/sites-enabled/.. // здесь лежат ссылки на файлы из папки /etc/nginx/site-available
			$ sudo ln -s /etc/nginx/sites-available/nextjs.conf /etc/nginx/sites-enabled/
	- 