#
	- [error] 8986#8986: *1144 upstream sent too big header while
		- add: Добавил в файл конфигурации nginx в ддиректорию location / {...}
			> proxy_buffer_size 128k; 
			> proxy_buffers 8 128k;
		- ref: https://stackoverflow.com/questions/33460569/nginx-proxy-buffering-changing-buffers-number-vs-size
	- 


server {
  server_name kopi34.ru www.kopi34.ru;
  location / {
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;    
    proxy_buffer_size 128k;
    proxy_buffers 8 128k;
  }