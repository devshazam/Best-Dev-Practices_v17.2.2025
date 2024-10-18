https://www.fossdex.com/new/deploying-full-stack-mern-application-on-an-nginx-vps/

1_ А-запись (АААА-запись):
        - $ping google.com // проверить А-запись домена
        - $curl ipinfo.io // для определения IP своего сервера

2_ ENV
    - $ sudo apt update
    - NVM - https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04#option-3-installing-node-using-the-node-version-manager 
            - $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
            - $ source ~/.bashrc
            - $ nvm install v18.15.0
    - $ npm install pm2 -g
    - $ sudo ufw allow 80 && sudo ufw allow 443 && sudo ufw allow 22 && sudo ufw enable && sudo ufw status

3_ NGINX
    - $ sudo apt install nginx
    - $ sudo rm /etc/nginx/sites-available/default
    - $ sudo rm -rf /var/www/html
    - $ sudo nano /etc/nginx/sites-available/app-name
    - $ sudo ln -s /etc/nginx/sites-available/seo /etc/nginx/sites-enabled/
    - "/etc/nginx/nginx.conf" - добавить переадресацию с www, увеличить размер загружаемых файлов

4_ DB 
    - DB // установка базы данных
    
5_ 
    - <git clone ... /var/www/> // клонирование всего проекта в папку контента nginx
        - git config --global credential.helper store
    - Frontend
        - <cd frontend; touch .env; nano .env> // вставить переменные среды фронта !!!! другой хост на проде
        - <npm install>
        - <npm run build>
    - Backend
        - <cd backend; touch .env; nano .env> // вставить переменные среды фронта
        - <pm2 start index.js>
        - ...
        - $sudo nginx -t
        - $sudo systemctl restart nginx.service 
            - or $sudo systemctl reload nginx


6_ CertBot



