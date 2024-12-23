# Тренд:
	- Server Action
		- Server and Client with SWR
			-- Ошибки из ServerAction НЕ передаются в catch вызвовшей ф-ции - она их не видит
				- Свойство swr error получает данные ошибки только если убрать try...catch в неудобном формате
				- https://joulev.dev/blogs/throwing-expected-errors-in-react-server-actions
			-- sentry не работает вместе с server action
			-- Нет собственного инструмента контроля за изменением данных после ревалидации (для работы оповещений например)
			-- middleware не работает
			-- cron задачи не работают
			-- Не работает POST c FormData

	- React_Query + API routs
        -+ sentry действует по умолчанию
    - axios
        - требуется использовать дополнительно useState + useEffect
    - fetch
        - требуется использовать дополнительно useState + useEffect
