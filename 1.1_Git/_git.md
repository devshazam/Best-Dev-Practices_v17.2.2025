# Клонирование
	$ git clone <repo address>
		--filter=blob:none // Флаг - запрещает скачивание больших двоичных файлов
	$ git clone --filter=blob:none --no-checkout <YOUR_CLONE_URL> // клонировать только конкретную папку

# Глобальная конфигурация
	git config --global credential.helper store
	git config --global user.name "devshazam"
	git config --global user.email "devshazam@gmail.com"

	git config --list // Список конфигурации

# Именование Git репозиториев:
	[product/project name]-[purpose]-[framework/language]


# Игнорировать файл после того, как его закоммитили
	- add file to gitignore
	- удалить файл их кеша
			$ git rm -r --cached <folder>
		OR
			$ git rm --cached <file>
	git status --ignored // получить список игнорируемых файлов и папок


# Работа с файлами	
	$ git rm text.txt // удалить файл из отслеживания
	$ git mv old.txt new.txt //  переименовать файл 
	$ git mv old/file.txt new/file.txt // переместить файл 

	$ git status
	$ git log
		$ git log -3 // отобразить последние 3 коммита
		- 
	$ git restore . // discard all unstaged changes in Git

	$ git add -A // индексация файла 
		$ git restore --staged file.txt // отмена индексации файла

	$ git commit -m "custom message"
		$ git commit -a -m "Updated index.html. Resized image" // коммит без команды add 
		$ git commit --amend // внесение изменений в коммит 1 сначала внести изменений; 2 индексировать их; 3 совершить команду


# Branches:
	$ git branch // вызвать имя текущей ветки
	$ git branch <branch-name> // создать новую ветку
		$ git branch -d <branch-name> // удалить ветку
		$ git push <remote_name> --delete <branch_name> // удаление удаленной ветки
		$ git branch --move old new // переименование веток 
			$ git branch -v // просмотр последнего коммита 
	$ git checkout <branch-name> // переключиться на ветку с именем <branch-name>
		$ git checkout -b <branch-name> // переключается на ветку или создает ее если ее нет
	$ git clone --single-branch --branch <branch-name> <remote-repo> // клонировать одну ветку определенного репозитория 
		$ git clone -b <branch> <remote_repo> // клонировать репозиторий с ветками

>	MERGE
	$ git merge <branch-name> // слияние веток: выполняется из той ветки в которую хотим слиять (она останется)
	$ git rebase master // преобразование веток

# GutHub
	$ git remote add origin <URL> // <URL> нужно взять при создании нового репозитория
		$ git remote show origin // просмотр информации о внешнем репозитории
		$ git remote // получение имени репозитория
		$ git remote -v // получение адреса внешнего репозитория
		$ git remote rename old new // переименование внешнего репозитороия
		$ git remote rm origin // удаление внешнего репозитория
		$ git remote show origin // информация о коротких командах
		
	$ git push --set-upstream origin master // отправить все локальное содержимое в GitHub
	$ git pull origin // получить все изменения и мерджить их. Состоит из двух команд
		$ git fetch origin //
		$ git merge origin/master
	$ git push
		$ git push -u origin master // просто полная версия команды
		$ git push origin master:remote_branch // отправить в другую ветку 
