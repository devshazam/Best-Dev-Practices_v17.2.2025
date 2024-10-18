`https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04-ru`

`https://selectel.ru/blog/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04/#installing-PostgreSQL`

```bash
# Install:
sudo apt update
sudo apt install postgresql postgresql-contrib

# Launch:	
# Start
sudo systemctl start postgresql.service
# Status
sudo systemctl status postgresql.service



# First entering: 

		- `sudo -i -u postgres` // by ubuntu superuser
			- postdrs@do:~$ // return new user 
				- postdrs@do:~$  `createuser --interactive` // create new postgres user
					- postdrs@do:~$  `createdb <user_name>` // create new DB !!! with user name
				- postdrs@do:~$  `psql`  // to switch to postgres terminal
					- postgres=# `\password postgres` // to set up a password for postgres

		- Add new user to ubuntu by superuser
			- `sudo adduser <user_name>` // create new superuser !!! with same name
	
# USAGE:
	- `sudo -i -u <user name>` // enter inside DB
	- start console postgers
		- `psql`
			# Закрыть консоль:
\q
# Информация о текущем соединении
\conninfo

			DataBase:
				- `\l` // show list of DB
					- `\l+` // show list of DB + more info
				- `\c database_name` // to switch DB
				- `DROP DATABASE database_name;` // to delete DB
					- `DROP DATABASE IF EXISTS database_name;`
				- 
			Tables:
				- `\dt` // show all tables of current DB
				- `SELECT * FROM <table_name>;` // to show data from table
				- `DROP TABLE <table_name>;` // to delete a table
					- `DROP TABLE IF EXISTS <table_name>;`
			Back up and restore DB:
				- https://www.freecodecamp.org/news/manage-postgresql-with-psql/#how-to-back-up-a-database-with-pg_dump

# Сменить кодировку кирилицы в консоли - когда кирилица не отображается корректно
\! chcp 1251

# Раббота с таблицами
\dt

SELECT * FROM <table_name>; // to show data from table
DROP TABLE <table_name>; // to delete a table
DROP TABLE IF EXISTS <table_name>; // to delete table if exist


https://www.freecodecamp.org/news/manage-postgresql-with-psql/
psql -d database_name -U username // подключение к pjstgresql  в терминале - !! sudo устанавливаться не надо!
Можно напрямую задавать пароль и остальное!!