# Ссылка на основной гайд: https://www.youtube.com/watch?v=Qu-oyzWIpjI&list=WL&index=3&t=1184s
	1) Развернуть VPS сервер Ubuntu 22.04

	2) Установить:
		- sudo apt update && sudo apt upgrade
		- sudo 
		- sudo apt install nginx
	3) FireWall
		$sudo ufw allow 'Nginx HTTP'
		$sudo ufw allow 'Nginx HTTPS'
		- разрешить SSH подключение по IP или полностью
		$sudo ufw enable
		$sudo ufw status
	5) Перенаправление домена на IP
		$systemctl status nginx // проверка работы nginx
		$curl ipinfo.io // проверка своего IP\

		- Конфигурационные файлы сервера nginx:
			$sudo nano /etc/nginx/sites-enabled/nextjs.conf
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
				$sudo rm /etc/nginx/sites-enabled/default
				- sudo nginx -t // ошибки синтаксиса
				$sudo ln -s /etc/nginx/sites-available/nextjs.conf /etc/nginx/sites-enabled/
				$sudo service nginx restart // Перезагрузка nginx для применения изменений
		- Конфигурация файла /etc/nginx/nginx.conf // разрешение загружать файлы более 1 Мб
	6) Установка ssl сертификаатов - https://beget.com/ru/kb/how-to/vps/vypusk-i-ustanovka-ssl-sertifikatov-ot-lets-encrypt-na-vps
			
