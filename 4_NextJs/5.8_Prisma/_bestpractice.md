## Установка https://www.prisma.io/docs/getting-started/quickstart
  1/3 `npm install prisma --save-dev` - установка зависимостей
  2/3 `npx prisma init` - авто конфигурация
    - .env подключение
      - DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
    - Создание database schema

  3/3 
    $ npx prisma migrate dev --name init - миграция
    - Создаст файл миграции в каталоге prisma/migrations. 
    - Создаст файл миграции SQL для базы данных. 
    - Запустит Prisma Generate под капотом (который установил пакет @prisma/client и создал специальный клиентский API Prisma на основе ваших моделей).


## Внесение изменений
  1_ prisma generate // каждый раз при внесении изменений в prisma shame нужно повторно генерировать  Prisma Client




















Errors:

  1_ Property 'errors' does not exist on type 'PrismaClient<PrismaClientOptions, nev
    - npx prisma generate
    - vsc reloading