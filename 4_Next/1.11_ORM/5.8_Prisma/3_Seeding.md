# Засеивание (Seeding) таблицы стартовыми данными:
	- ⚠️при использованиии команды "npx prisma bd seed" 
		- ⚠️не работает импорт в typescript файлах из-за конфликта "Cannot redeclare block-scoped variable" - эта ошибка специфична для ts
			- Решение все данные нужно держать в одном файле!
			- Решение (не эффективное) https://medium.com/@surajkpcool/cannot-redeclare-block-scoped-variable-in-typescript-b92454f2f81f
	- Для работы с typescript Установить npm i -D ts-node typescript @types/node 
	- Добавить в package.json:
		- Для commonJs модулей 
			"prisma": { "seed": "ts-node prisma/seed.ts" }
		- Для ECMAScript модулей
			"prisma": { "seed": "node --loader ts-node/esm prisma\seed.ts" }
	- Запустить команду:
		$ npx prisma db seed

