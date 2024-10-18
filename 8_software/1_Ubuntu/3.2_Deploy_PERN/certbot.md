Работа с сертификатами:
    $ sudo certbot --nginx // выпустить сертификат
    $ certbot certificates // проверить статус сертификатов 
    $ certbot renew --force-renewal // Обновить сертификат 
        - https://dvmn.org/encyclopedia/deploy/renewing-certbot-certificates-for-nginx-using-a-systemd-timer/#update-certificates-manually
    $ sudo certbot delete // удаление сертификата из списка









==================================

Ошибки: 
    - Error_description: Hint: The Certificate Authority failed to verify the temporary nginx configuration changes made by Certbot. Ensure the listed domains point to this nginx server and that it is accessible from the internet. 
        - У домена две, разные А-записи: а-запись и АААА-запись ведущие на разные IP адреса - один нужно удалить!
            # https://community.letsencrypt.org/t/the-certificate-authority-failed-to-ri-the-temporary-nginx-configuration-changes-made-by-certbot/181348
        - FireWall - я закрыл HTTP протокол, поэтому я не смог исполнить команду обновления сертификата!
            # https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04


