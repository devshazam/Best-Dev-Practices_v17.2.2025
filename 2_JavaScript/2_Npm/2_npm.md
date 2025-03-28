#
    - Установка/Удаление:
		$ npm i <package-name> // установка в dependencies
			--only=dev // только devDependencies
			--production // только dependencies
		$ npm i <package-name> --save-dev // установка в devDependencies
		$ npm i <module_name> -P // перенести пакет в dependencies
		$ npm i <module_name> -D // перенести пакет в devDependencies
		$ npm uninstall <package-name>
	- Обновление до последней версии
		$ npm install -g npm-check-updates
			$ ncu --upgrade
			$ npm install


# Пакеты установки	
	$ npm i next-auth@beta @auth/prisma-adapter @prisma/client uuid zod bcryptjs
	$ npm i prisma @types/uuid autoprefixer @types/bcryptjs --save-dev