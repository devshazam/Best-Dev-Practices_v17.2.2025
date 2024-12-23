#
	- При выборе файлов через Input мы получаем массив объектов File в fileList
		- File это объект хранящий информацию о файле без самого файла
			- Создать ссылку на файл в оперативной памати link.href = URL.createObjectURL(File);
			- Освободить память URL.revokeObjectURL(link.href);

	-  Binary Large Object BLOB