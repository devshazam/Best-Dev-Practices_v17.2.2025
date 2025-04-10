# Управление FireWall
    - https://selectel.ru/blog/tutorials/how-to-configure-firewall-with-ufw-on-ubuntu-20/


	- Allow:
	$ sudo ufw allow 'Nginx HTTP'
	$ sudo ufw allow 'Nginx HTTPS'
	$ sudo ufw allow from 88.87.92.132 to any port 22
		- Рабочий IP: 88.87.92.132
	
	$ sudo ufw show added


	$ sudo ufw enable // ⛔ если не разрешить ssh, то тебя заблокирует
    	$ sudo ufw disable // Деактивировать FireWall

    $ sudo ufw status numbered // показать список запретов 
        $ sudo ufw delete 3 // удалить запреты из списка выше

