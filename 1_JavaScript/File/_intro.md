#
	- При выборе файлов через Input мы получаем массив объектов File в fileList
		- File это объект хранящий информацию о файле (и разрешение его скачать) без самого файла
			- Создать ссылку на файл в оперативной памати link.href = URL.createObjectURL(File);
			- Освободить память URL.revokeObjectURL(link.href);

	-  Binary Large Object BLOB
	- FileReader - это асинхронный API для обработки объектов File и Blob
		- readAsText() - метод для чтения объекта файла как обычного текста
		- readAsDataURL() - метод создает URL к файлу в памяти
		- readAsArrayBuffer() - считывает содержимое файла в буыыер массива
```js
		const getBase64 = (file: FileType): Promise<string> =>
			new Promise((resolve, reject) => {
				const reader = new FileReader();
				reader.readAsDataURL(file);
				reader.onload = () => resolve(reader.result as string);
				reader.onerror = (error) => reject(error);
			});
```