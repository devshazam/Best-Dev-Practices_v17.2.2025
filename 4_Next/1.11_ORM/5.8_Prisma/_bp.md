## Установка  
    - ref: https://www.prisma.io/docs/orm/prisma-client/setup-and-configuration/introduction
    $ npm install prisma --save-dev // установка зависимостей
    $ npx prisma init// авто конфигурация
      - .env подключение
        - DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
      - Создание database schema
    $ npm install @prisma/client
    $ npx prisma migrate dev --name init // ⛔инициирующая миграция
      - ⛔УДАЛЯЕТ ВСЕ ДАННЫЕ ИЗ БД⛔
      - Создаст файл миграции в каталоге prisma/migrations. 
      - Создаст файл миграции SQL для базы данных. 
      - Запустит Prisma Generate под капотом (который установил пакет @prisma/client и создал специальный клиентский API Prisma на основе ваших моделей).


## Внесение изменений в shema.prisma
  $ npx prisma db push // каждый раз при внесении изменений в prisma shame нужно повторно генерировать Prisma Client
    - Вносит изменения в БД без удаления данных 
    - Генерирует Prisma Client (аналогично команде $ prisma generate)
  		$ prisma generate // отдельное использование на имеет смысла т.к. не применяет изменения к БД 