https://medium.com/django-unleashed/django-deployment-on-vps-server-a81b581d3fab
https://codewithmuh.medium.com/deploy-django-project-on-digital-ocean-vps-droplet-ca6f88aa3ade
https://codewithmuh.medium.com/deploy-django-project-on-digital-ocean-vps-droplet-ca6f88aa3ade

1_ Install packages
    apt update
    sudo apt install -y nginx
    sudo apt install -y python3 python3-pip
    sudo pip3 install virtualenv

2_ Install project
    cd /app
    git clone ...
    cd /app/myip-multi-framework/
    virtualenv --python=python3 venv
    source venv/bin/activate
    pip3 install -r requirements.txt

2.1_ Install 
    pip install django gunicorn

4_ Configuring
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic

    python manage.py createsuperuser

4.1 env
    nano .env

5_ Gunicorn
    sudo nano /etc/systemd/system/your_domain.gunicorn.socket

6_ SECURITY
    firewall // включить фаервол
    allow_host // ограничить хостыckjgf