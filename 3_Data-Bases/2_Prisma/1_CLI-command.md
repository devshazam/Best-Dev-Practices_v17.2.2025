# Установка  
    $ npm install prisma --save-dev
    $ npx prisma init
    $ npm install @prisma/client
    $ npx prisma migrate dev --name <name> // Создать миграцию при внесении изменений в shema
      - Создаст файл миграции в каталоге prisma/migrations. 
      - Создаст файл миграции SQL для базы данных.

## Дополнительные команды:
	$ prisma migrate reset // Удалить все из БД и запустить seeding ⛔в Supabase не работает
		$ npx prisma db seed // запускает seeding
	$ prisma generate // генерирует клиент


		