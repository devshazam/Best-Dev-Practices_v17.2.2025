# Тренд:
	- Fetching:
		- Server Side
			- fetch() - вызов внешних API (Публичные / Защищенные)
			- orm db call - вызов базы данных напрямую
		- Client Side
			- useEffect + fetch - вызов собственных API сайта

	- Server Action:
		- Server Side
			- Внешние API (Публичные / Защищенные)
				- fetch, 
			- Data Bases - напрямую
			- Server Actions (функции вызываемые атрибутом action form)
		- Client Side
			- API свой сервер
				- ReactQuery
				- Fetch
				- Axios
			- Server Action
				- SWR

# Паралельная и последовательная выборка

	- Server Action
		- Общие Ограничения Server Action
			-- Vercel - ограничение на размер тела ф-ции 
				- https://vercel.com/docs/functions/runtimes#request-body-size
		- Server and Client with SWR
			-- Ошибки из ServerAction НЕ передаются в catch вызвовшей ф-ции - она их не видит
				- Свойство swr error получает данные ошибки только если убрать try...catch в неудобном формате
				- https://joulev.dev/blogs/throwing-expected-errors-in-react-server-actions
			-- sentry не работает вместе с server action
			-- Нет собственного инструмента контроля за изменением данных после ревалидации (для работы оповещений например)
			-- middleware не работает
			-- cron задачи не работают
			-- Не работает POST c FormData
		- Server Action Only
			- Вызов с Server = асинхронный вызов в теле главной ф-ции
			- Вызов с Client = асинхронный вызов при событии onClick или через useEffect
	- React_Query + API routs
        -+ sentry действует по умолчанию
    - axios
        - требуется использовать дополнительно useState + useEffect
    - fetch
        - требуется использовать дополнительно useState + useEffect
