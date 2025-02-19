# INSTALL
	- https://help.reg.ru/support/servery-vps/oblachnyye-servery/ustanovka-programmnogo-obespecheniya/kak-ustanovit-i-nastroit-redis-na-linux#2
	$ sudo apt update && sudo apt upgrade
	$ sudo apt install redis-server

## CONFIG
	$ sudo nano /etc/redis/redis.conf
		- Заменить директиву supervised на systemd
			> supervised systemd
	$ sudo systemctl restart redis.service

## TESTING
	$ sudo systemctl status redis // проверка статуса работы

