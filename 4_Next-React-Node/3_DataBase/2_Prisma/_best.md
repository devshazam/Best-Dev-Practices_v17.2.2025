## Установка  
    $ npm install prisma --save-dev
    $ npx prisma init
    $ npm install @prisma/client
    $ npx prisma migrate dev --name init // ⛔инициирующая миграция
      - ⛔УДАЛЯЕТ ВСЕ ДАННЫЕ ИЗ БД⛔
      - Создаст файл миграции в каталоге prisma/migrations. 
      - Создаст файл миграции SQL для базы данных. 
      - Запустит Prisma Generate под капотом (который установил пакет @prisma/client и создал специальный клиентский API Prisma на основе ваших моделей).

## Внесение изменений в shema.prisma
  	$ npx prisma db push // Вносит изменения в БД без удаления данных и генерирует клиент
		$ prisma generate // генерирует клиент
	$ prisma migrate reset // Удалить все из БД и запустить seeding ⛔в Supabase не работает
		$ npx prisma db seed // запускает seeding