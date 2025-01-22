# Режим сборки
	mode: 'development', // режим сборки ('development', 'production')
		- режим сборки можно задавать через package.json  (cм пример)
		- режим 'WATCH' - можно задавать через package.json (cм пример)
	entry: './src/index.js', // точка входа - файл который стартует приложение
	output: { filename: 'build.[contenthash].js', } // точка выхода
		- [contenthash] - добавить в название хеш - для решения проблемы хешей
		- по умолчанию '/dist/main.js'
# Плагины
	plugins: [
		new TestWebpackPlugin1(),
		new TestWebpackPlugin2()
	],

# Лоадеры
	⛔Лоадеры выполняются по очереди. При этом очередь начинается с конца массива. То есть первым выполняется лоадер, указанный последним элементом массива, потом предпоследим и так далее!
	- Стили
		$ npm install css-loader --save-dev
		$ npm install style-loader --save-dev
```js
	module: {
		rules: [
			{
				test: /\.css$/i,
				use: ['style-loader', 'css-loader'],
			},
		],
	},
```


Привет! Правки по сайту подъехали) 

2. Убираем solo renovación.


9. Выход из галереи смахиванием вниз.

11. Добавить кнопку вверх. 