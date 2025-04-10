# Установка CertBot
    $ sudo apt install certbot
		https://docs.vultr.com/how-to-install-nginx-web-server-on-ubuntu-24-04

# Работа с сертификатами:
    $ sudo certbot --nginx // выпустить сертификат
    $ certbot certificates // проверить статус сертификатов 
    $ certbot renew --force-renewal // Обновить сертификат 
        - https://dvmn.org/encyclopedia/deploy/renewing-certbot-certificates-for-nginx-using-a-systemd-timer/#update-certificates-manually
    $ sudo certbot delete // удаление сертификата из списка

# Нахождение логов 
    $ nano /var/log/letsencrypt/letsencrypt.log

# certbot_errors : 
    - Error_description: Hint: The Certificate Authority failed to verify the temporary nginx configuration changes made by Certbot. Ensure the listed domains point to this nginx server and that it is accessible from the internet.
        - Error_resolve_link: https://community.letsencrypt.org/t/the-certificate-authority-failed-to-verify-the-temporary-nginx-configuration-changes-made-by-certbot/181348
        - Error_resolve: There was two diferent IP - A-record (IP4) and AAAA-record (IP6) - I have deleted AAAA-record
    - ImportError: cannot import name 'appengine' from 'requests.packages.urllib3.contrib' 
        - ref: https://stackoverflow.com/questions/76554745/certbot-cannot-import-name-appengine-from-urllib3-contrib
        - sol: pip3 uninstall urllib3
    - Certbot failed to authenticate some domains (authenticator: nginx).
        - sol: Нужно отключить Фаервол для проведения операции
    - nginx: [emerg] cannot load certificate "/etc/letsencrypt/live/telebot7.kopi34.ru/fullchain.pem":
        - нужно удалить из nginx конфига блок server{...} сгенерированный certbot