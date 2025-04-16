# Тренд
https://npmtrends.com/drizzle-orm-vs-prisma-vs-sequelize-vs-typeorm

	- PostgreSQL
		- Prisma
			-+3 По умолчанию поддерживается и оптимизирована под NextJs, SupaBase; Читабельная документация; В отличаи от МонгоДБ дефолтные ID цифровые и по порядку!
		- Drizzle (drizzle-orm)
		- Sequalize
			-+1 В отличаи от Prisma есть метод getAndCount

		- TypeOrm
		- SQL (SupaBase + FireBase)
			-- переусложнен
	- MongoDB
		- Mongoose
			-+0 
	- SQLite (для микро-сервисов)
		- Sqlite3
	- ClickHouse
	- RabbitMQ


<!-- Не рекомендуется к использованию (интенсивно устаревает) -->
	- MySQL
		-- Слишком мнго недостатков по сравнению с PostgreSQL, что бы их перечислять!