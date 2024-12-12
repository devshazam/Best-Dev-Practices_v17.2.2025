# Клонирование
	$ git clone <repo address>
		--filter=blob:none // Флаг - запрещает скачивание больших двоичных файлов

# Глобальная конфигурация
	git config --global credential.helper store
	git config --global user.name "devshazam"
	git config --global user.email "devshazam@gmail.com"

	git config --list // Список конфигурации

# Именование Git репозиториев:
	[product/project name]-[purpose]-[framework/language]


# Игнорировать файл после того, как его закоммитили
	add file to gitignore
	git rm -r --cached <folder>
	git rm --cached <file>
	git status --ignored // получить список игнорируемых файлов и папок

# Скопировать только выбранную папку:
	git clone --filter=blob:none --no-checkout <YOUR_CLONE_URL>
		git clone --filter=blob:none --no-checkout

# ОШИБКИ:
    - При переименовании при котором меняется только регистр букв - гит не увидит этого!
        : <git mv old-file-name.ts new-file-name.ts>
