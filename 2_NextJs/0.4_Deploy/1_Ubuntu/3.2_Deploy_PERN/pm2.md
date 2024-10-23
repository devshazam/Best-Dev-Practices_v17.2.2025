- $ sudo npm install -g pm2

- $ pm2 startup // Запускать автоматически при запуске или перезапуске системы (хостинга VPS)
  - $ pm2 save

- $ pm2 start index.js --name myname --time --watch // запуск под именем
        --time // для вставки времени в логи ошибок 
        --name <name> // для именования 
        --watch // перезагружать приложение при изменении файлов !!! я делфю в ручную

- $ pm2 logs <appname> --lines 40 // журналы appname приложения по 40 строк
  - $ pm2 flush - очиститть журналы



