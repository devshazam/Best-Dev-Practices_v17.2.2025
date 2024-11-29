# Введение
	- SQL Editor
		- Работает с обычным SQL
			- Изменить Юзера:
				update auth.users
				set "is_super_admin" = true
				where id = '0d32326a-2b72-40f4-ba2b-f246d03b4058'
			- Получить Юзера:
				select * from auth.users where id = '0d32326a-2b72-40f4-ba2b-f246d03b4058'