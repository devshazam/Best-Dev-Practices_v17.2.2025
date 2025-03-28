# Ссылка на основной гайд: https://www.youtube.com/watch?v=Qu-oyzWIpjI&list=WL&index=3&t=1184s
	1. Git clone
	2. Установка зависимостей
		$ npm install
	3. Создание файла .env
		$ nano .env
		- заменить переменные:
			- NODE_ENV="development"
			- NEXT_PUBLIC_APP_URL="https://kopi34.ru" 
	4. Построение next
		$ npm run build
	5. Запуск pm2
		$ pm2 start npm --name <app-name> --time -- start