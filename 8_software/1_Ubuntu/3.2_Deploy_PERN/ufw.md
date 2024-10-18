
    - sudo ufw allow from 80.90.179.8 to any port 22 // разрешить подключение к ssh только выбранному IP
    - sudo ufw allow from 88.87.92.132 to any port 22 // разрешить подключение к ssh только выбранному IP
    - sudo ufw status numbered // показать список запретов 
        - sudo ufw delete 3 // удалить запреты из списка выше

    # https://selectel.ru/blog/tutorials/how-to-configure-firewall-with-ufw-on-ubuntu-20/
