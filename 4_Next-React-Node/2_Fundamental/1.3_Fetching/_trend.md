# Выбор:
>>  - SWR + server action
        -+ минималистичность кода
		-- sentry не работает вместе с server action
		-- Свойство error получает данные ошибки только если убрать try...catch в неудобном формате
>>  - React_Query + API routs
        -+ sentry действует по умолчанию
    - axios
        - требуется использовать дополнительно useState + useEffect
    - fetch
        - требуется использовать дополнительно useState + useEffect
