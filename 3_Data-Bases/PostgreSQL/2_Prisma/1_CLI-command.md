# Установка - development
    $ npm install prisma @prisma/client --save-dev
    $ npx prisma init // создание файла schema.prisma
    $ npx prisma migrate dev --name init
      - Создаст файл миграции в каталоге prisma/migrations. 
      - Создаст таблицы в БД 

# Установка - prod/docker
	$ npx prisma generate // сгенерирует клиент на продакшене

## Дополнительные команды:
	$ npx prisma db seed // запускает seeding БД
	$ prisma migrate reset // Удалить все из БД и запустить seeding ⛔в Supabase не работает


		