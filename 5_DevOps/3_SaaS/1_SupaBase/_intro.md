# Intro
	_feature:
		- AUTH
			- БД делиться на две части 'public' и остальные
				- 'public' - открытая, все таблицы доступны для изменения и чтения
				- БД AUTH является защищенной 
					- доступ 
		- DataBase - По умолчанию используется язык SQL (преимущество в том, что можно использовать закрытые библиотеки например 'auth.users' в качестве ассоциации по пути '@/supabase/...':
			- https://github.com/JessicaFM/supabase-todolist/tree/main
			- https://github.com/DevWedeloper/nextjs-supabase-todo/tree/main
			- https://github.com/Hurly77/Todos/tree/main
			- https://github.com/vercel/nextjs-subscription-payments/tree/main
		Также есть  встроенная возможность создавать миграции и сиды:
			- npx supabase init // для инициализации
			- npx supabase login // для аутентификации
			- npx supabase link .. для подключения к выбраной ДБ
			- npx supabase migration new init // создание нового файла миграции (пустого!)
			- npx supabase db push