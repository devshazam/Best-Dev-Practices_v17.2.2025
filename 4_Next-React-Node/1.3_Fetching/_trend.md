# Тренд:
	- Server Action
		- From Server (Only Server action - call from await OR form-action)
			- Ошибки из ServerAction НЕ передаются в catch вызвовшей ф-ции - она их не видит
				- https://joulev.dev/blogs/throwing-expected-errors-in-react-server-actions
		- From Client
			- SWR
				-+ минималистичность кода
				-- sentry не работает вместе с server action
				-- Свойство swr error получает данные ошибки только если убрать try...catch в неудобном формате
				-- middleware не работает на 
>>  - React_Query + API routs
        -+ sentry действует по умолчанию
    - axios
        - требуется использовать дополнительно useState + useEffect
    - fetch
        - требуется использовать дополнительно useState + useEffect
