# Тренд:
>>  - SWR + server action
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
