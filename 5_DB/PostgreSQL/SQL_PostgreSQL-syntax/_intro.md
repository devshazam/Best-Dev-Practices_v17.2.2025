# https://www.w3schools.com/postgresql/index.php
	- Structured Query Language
	- Features
		- SQL keywords are NOT case sensitive
			-  ключевые слова желательно выделять капсом для лучшей читаемости
		- Semicolon after SQL Statements;
			- 
		- Текстовые, числовые поля и boolean поля
			'1', 1, true
	
### SELECT * FROM <table_name> // выбрать все поля из базы данных
		- SELECT <field_name1>, <field_name1>, ... FROM <table_name> // для выбора определенных полей из таблицы
		- SELECT COUNT(DISTINCT country) FROM customers; // вернет кол-во разных названий стран из таблицы customers и поля country
	- WHERE - выбрать все где значение поля соответствует условию
		- '=','>','<'','<=','>=','<>','!='
		- WHERE Price BETWEEN 50 AND 60; // между значениями
		- WHERE City IN ('Paris','London'); // один из списка
		- WHERE City LIKE 's%'; // поиск по регулярным выражениям
		- WHERE column_name IS NULL;
			- WHERE column_name IS NOT NULL;
		+ AND
			- WHERE Country = 'Spain' AND CustomerName LIKE 'G%';
		+ OR
			- WHERE Country = 'Germany' OR Country = 'Spain';
		+ NOT
			- WHERE NOT Country = 'Spain';
	- ORDER BY Country ASC, CustomerName DESC;
	- LIMIT 20 OFFSET 40;
 
	- EXISTS // ставит выражение в зависимость от истинности запроса 
	- ANY // ставит в зависимость от кол-ва записей с определенными условиями
		- ALL // тоже
	- CASE // условное исполнение

### INSERT INTO <table_name> (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
		- INSERT INTO table_name VALUES (value1, value2, value3, ...); // для вставки всех полей в таблицу

### UPDATE <table_name> SET column1 = value1, column2 = value2, ... WHERE condition;
	⛔ Если обновление происходит не по ID - то высок риск сделать массовое изменение

### DELETE FROM <table_name> WHERE condition;
	⛔ Если обновление происходит не по ID - то высок риск сделать массовое изменение

## FUNCTIONS
	- Min, Max // выдаст минимальное/максимальное значение из определенного столбца
	- COUNT // выдаст общее кол-во строк по заданным фильтрам
	- SUMM // выдаст сумму по определенным колонкам
	- AVR // выдаст среднее значение
	+ HAVING SUM(products.price) > 400.00; // выражение добавляется в конце - если условие true - то весь запрос выполняется, если нет - то нет!
