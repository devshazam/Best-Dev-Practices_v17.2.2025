#
	- Request
		- req.path // выведет '/dir/page.html'
		- req.url // выведет '/dir/page.html?get1=1&get2=2'
		- req.originalUrl // выведет '/dir/page.html?get1=1&get2=2' В отличае от url его нельзя изменить средствами expressэ
		- req.query // содержит объект {get1: '1', get2: '2'}
			- req.query.get1 // выведет '1'
		- req.protocol // выведет 'http' или 'https'
			- req.secure // выведет false если 'http'
		- req.headers // выведет заголовки
		- req.ip // IP пользователя
	
	- Response
		- res.status(404).send('not found');
		- res.redirect(301, '/');
		- res.type('text/plain'); res.send('hello world');
		- res.sendFile(__dirname + '/page.html');
			- import __dirname from './dirname';
				- process.cwd()
			- При запросе не существующего файла будет ошибка
				import fs from 'fs/promises';
				import { constants } from 'fs';
				app.get('/page/:num/', function(req, res) {
					let path = __dirname + '/pages/' + req.params.num + '.html';
					
					fs.access(path, constants.F_OK).then(() => {
						res.sendFile(path);
					}).catch(() => {
						res.status(404).send('not found');
					});
				});
	
	- Статические файлы:
		- app.use(express.static(__dirname + '/public/'))

	- Роутинг
		- При конфликте маршрутов побеждает первый
		- app.get('/test/:num1/:num2/', function(req, res) {
				res.send(req.params.num1 + ' ' + req.params.num2);
			});
			- Необязательные 
				- app.get('/test/:num?/', function(req, res) { });
		- Регулярные выражения можно использовать +, *, ?, ():
			- app.get('/user(name)?', function(req, res) { });
			- app.get(/admin|user(name)?/, function(req, res) { });
		
	- Cron  - https://dev.to/thesohailjafri/how-to-schedule-cron-job-in-nodejs-expressjs-2flm