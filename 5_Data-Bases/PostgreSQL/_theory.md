# Export:
	- Перемещение БД
		- Через экспорт/импорт дампа базы данных (дамп помимо данных таблиц содержит доп. информацию: о текущем инкременте id в таблицах). Дамп SQL включает такие данные как:
			- Номера счета id (auto increment id) для полей со значением по умолчанию autoincrement
			- 
		- Импорт на уровне таблицы в Adminer предполагает ручное управление:
			- задать Номера счета id (auto increment id) для полей со значением по умолчанию autoincrement:
				SQL: ALTER SEQUENCE "<Table-name>_id_seq" RESTART WITH 56;
				- https://stackoverflow.com/questions/62010838/reset-postgres-auto-increment-value-to-0