install certbot
    https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
    
    https://beget.com/ru/kb/how-to/vps/vypusk-i-ustanovka-ssl-sertifikatov-ot-lets-encrypt-na-vps#nginx
launch certbot - certificat
    sudo certbot --nginx

certbot_errors : 
    - Error_description: Hint: The Certificate Authority failed to verify the temporary nginx configuration changes made by Certbot. Ensure the listed domains point to this nginx server and that it is accessible from the internet.
    - Error_resolve_link: https://community.letsencrypt.org/t/the-certificate-authority-failed-to-verify-the-temporary-nginx-configuration-changes-made-by-certbot/181348
    - Error_resolve: There was two diferent IP - A-record (IP4) and AAAA-record (IP6) - I have deleted AAAA-record