## Error: P3014
<<<<<<<< HEAD:5_Data-Bases/PostgreSQL/2_Prisma/_errors.md
	- ref
	- desc = В Облочных базах данных нужно дополнительное разрешение
	- sol
========
    - ref
    - desc = В Облочных базах данных нужно дополнительное разрешение
    - sol:
>>>>>>>> 543a34ef18026ddfb7b12752f3b0b6db5cbe6683:3_Data-Bases/PostgreSQL/2_Prisma/_errors.md
		- добавить shadowDatabaseUrl = env("SHADOW_DATABASE_URL") в datasource db{ }
		- добавить в env переменную SHADOW_DATABASE_URL= с тем же значением ч

## Error: can't creat additional DB client
	- REF - https://www.prisma.io/docs/orm/more/help-and-troubleshooting/help-articles/nextjs-prisma-client-dev-practices
	- desc - Создание больше чем 10 экземпляров prismaClient на всех ПК в интернете к облачной БД PostgresQL создает такую проблему
	- sol - применил изменения