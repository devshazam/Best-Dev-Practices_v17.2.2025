1. File SHell
	- #!/bin/bash // первая строка - ссылка на исполняемый файл (можно выбрать другой)
	- # // комментарий
	- 

1. Commands:
	$ rm -rf app // удалени файлов и папок рекурсивно 
	$ mv book_list.txt movie_list.txt // в текущей папке
		$ cp  // Копировать файл или каталог
	$ > file.md // очистить содержимое файла

	$ echo -e "\nenter the path to directory" // вывод строки с переносом строки

	$ nano test.txt // возможно редактирование кода вставка 
	$ cat test.txt // Отображение содержимого файла

	$ grep <search-word> /var/log/auth.log // поиск по файлу
	$ tail -15 mylogfile.txt // вывод 15 последних строк

	$ history | grep <search-word>
		!<command-number> // вбить номер команды для повторения

	$ ping domail.com // проверка привязанного IP адреса домена


2. Options:
	- && // исполнить при условии успешного исполнения предыдущей команды
		- ; // выполнить все в не зависимости от результата предыдущих
		- || // выполнить одно из многих, остальные не выполнять
	- > // перенаправление результатов команды в файл
	- | // перенаправление результатов команды в следующую команду

3. Исполнение .sh файлов
	$ sh script.sh
	$ . ./script.sh