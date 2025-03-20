# Установка - development
   	$ npm install @prisma/client --save-dev
		- автоматически генерирует клиент в каталог '/node_modules/.prisma/client' (npx prisma generate)
	$ npm install prisma
	$ npx prisma init // создание файлов schema.prisma и записи в .env 
	$ npx prisma migrate dev --name init
		- Создаст файл миграции в каталоге prisma/migrations. 
		- Создаст таблицы в БД 

# Установка - prod/docker
	$ npx prisma generate // сгенерирует клиент на продакшене

## Дополнительные команды:
	$ npx prisma db seed // запускает seeding БД
	$ prisma migrate reset // Удалить все из БД и запустить seeding ⛔в Supabase не работает

# Подключение к существующей БД
	$ npx prisma db pull