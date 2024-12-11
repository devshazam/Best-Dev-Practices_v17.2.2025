## Error: P3014
    - ref = https://github.com/prisma/prisma/issues/13275
    - desc = В Облочных базах данных нужно дополнительное разрешение
    - sol = добавить `shadowDatabaseUrl = env("SHADOW_DATABASE_URL")` в env и в shema

## Error: 001
	- REF - https://www.prisma.io/docs/orm/more/help-and-troubleshooting/help-articles/nextjs-prisma-client-dev-practices
	- desc - Создание больше чем 10 экземпляров prismaClient на всех ПК в интернете к облачной БД PostgresQL создает такую проблему
	- sol - применил изменения