1. Установка
   	$ npm install @prisma/client --save-dev
		- автоматически генерирует клиент в каталог '/node_modules/.prisma/client' (npx prisma generate)
	$ npm install prisma
		- ⛔вставить в packedge.json scripts: "postinstall": "prisma generate"
	$ npx prisma init // создание файлов schema.prisma и записи в .env 
	- ⛔ ВАЖНО: теневая ДБ должна быть отдельной в "schema.prisma"
	$ npx prisma generate // сгенерирует клиент

2. Миграции 
	$ npx prisma migrate status 
		- ♻️⛔проверить статус синхронизации миграций в БД и в папке "prisma/migrations"
	$ npx prisma migrate dev --name init 
		- ⛔ Команда миграции может удалить все данные, если миграции не синхронизованы, перед ее использованием "npx prisma migrate status"
		- Создаст файл миграции в каталоге "prisma/migrations" 
		- Создаст таблицы в БД 
	$ npx prisma migrate dev --name add_new
		- ⛔ Команда миграции может удалить все данные, если миграции не синхронизованы, перед ее использованием "npx prisma migrate status"
		- Обновляет миграцию после внесения изменений в "schema.prisma", ⛔ВАЖНО: БД не должна быть пустой для ее работы, но добавлять изменения можно только с дефолтными значениями или null (пример test String?)

	2.1 Подключение к существующему проекту
		$ npx prisma db pull 
			- получить схему удаленной БД и записать ее в  "schema.prisma"
		$ mkdir -p prisma/migrations/0_init
			- создать папку "prisma/migrations/0_init"
		$ npx prisma migrate diff --from-empty --to-schema-datamodel prisma/schema.prisma --script > prisma/migrations/0_init/migration.sql 
			- создает локальную миграцию в "prisma/migrations"
		$ npx prisma migrate resolve --applied 0_init
			- задать статус миграции как "Выполненная"
			- создать таблицу миграции в БД
3. Дополнительные команды:
	$ npx prisma db seed // запускает seeding БД
	$ prisma migrate reset // Удалить все из БД и запустить seeding ⛔в Supabase не работает

# Подключение к существующей БД
	$ npx prisma db pull