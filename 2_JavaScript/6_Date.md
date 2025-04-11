1. Получение Full Text String:
	 Date(); 
	 	// 'Fri Apr 11 2025 10:43:28 GMT+0000 (Coordinated Universal Time)'

2. ISO Format:
	- new Date();
	- new Date('Fri Apr 11 2025 10:43:28 GMT+0000 (Coordinated Universal Time)');
		- new Date('August 14, 2022 14:15:30')
	- new Date("2015-03-25");
	- new Date("2025-04-11T10:43:28.000Z");
	- new Date(year, month, day?, hours?, minutes?, seconds?, millisec?)

2.1 GET LOCAL (в поясе браузера):
	- date.getTime(); // return :Number кол-во миллисекунд с 01.01.1970
	- date.getDate(); // return :Number from 1 to 31
		- и так далее годы, месяцы ... 

2.2 GET UTC (время в Лондоне)
	- date.getUTCDate(); // return :Number кол-во миллисекунд с 01.01.1970
		- и так далее годы, месяцы ... 

2.3 CONVERT:
	- date.getTime(); // return :Number кол-во миллисекунд с 01.01.1970
	- date.toJSON(); // return :String ISO "2025-04-11T10:43:28.000Z"
	- date.toISOString(); // return :String ISO "2025-04-11T10:43:28.000Z"
	- date.toString(); // return :String Full Text String "Fri Apr 11 2025 15:10:53 GMT+0300 (Волгоград, стандартное время)"

2.4 ЛОКАЛИЗАЦИЯ:
	- date.toLocaleDateString(); // return :String "11.04.2025" в России
	- date.toLocaleTimeString(); // return :String "15:13:43" в России
	- date.toLocaleString(); //  return :String "11.04.2025, 15:14:14" в России

3. Milliseconds
	- Date.now() // кол-во миллисекунд с 01.01.1970 до текущего момента
	- Date.parse("March 21, 2012") // кол-во миллисекунд с 01.01.1970 до "March 21, 2012"
	- Date.UTC(year, month, day?, hours?, minutes?, seconds?, millisec?) // кол-во миллисекунд с 01.01.1970 до этого времени