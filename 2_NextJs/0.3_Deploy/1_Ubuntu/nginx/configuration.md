
RESTARTING: 
        https://owlhowto.com/how-to-increase-file-upload-size-on-nginx/
    sudo nginx -t // check nginx syntax
    sudo nginx -s reload // only reload nginx.conf without restart nginx server
        (https://stackoverflow.com/questions/42451592/how-to-restart-nginx-in-ubuntu-or-other-linux-servers)
    sudo systemctl restart nginx // restart nginx server
    sudo service nginx restart

Increase File Upload Size on Nginx:
        https://owlhowto.com/how-to-increase-file-upload-size-on-nginx/
    client_max_body_size 50M;

Redirect from www to without www - https://help.reg.ru/support/klassicheskie-vps/osnovi-raboty-s-vps/nastroyka-redirekta-s-pomoshchyu-nginx-na-vps
     
     
Folders:
    /etc/nginx/nginx.conf
        - nginx.conf // здесть все настройки сервера nginx, но для каждого сайта можно сделать еще один конфигурационный файл в папке sites-available
            - sites-available/defualt

