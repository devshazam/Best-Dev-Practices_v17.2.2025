## Fetch: 
    - const { data, error, isLoading } = useSWR(key, fetcher)
        - Обычно в качестве ключа передают url, потому что он уникален
        - data - данные имеют три состояния
            - undefined - в процессе получения
            - `some data` - при успешном получении
            - undefined - при ошибке
        - error - данные об ошибке
            - undefined - в процессе получения
            - undefined - при успешном получении
            - `some data` - при ошибке
        - isLoading - boolean - показатель прогресса загрузки
            - true - в процессе получения
            - false - при успешном получении
            - false - при ошибке
        - key - ключ кеширования ⚠️должен быть уникален для разных запросов, иначе будет возвращать одинаковый ответ
        - fetcher - функция 
    - SWR нужен для работы на клиенте (на сервере не работает!)
    - Работает с Server Action - вызывает напрямую импортированную ф-цию из директории `@lib/...`
    - Кеширует по умолчанию - поэтому 

## Fetch with arguments
    - const { data, error, isLoading } = useSWR('/api/user', url => fetcher(url))
    - const { data, error, isLoading } = useSWR(`${x1}`, url => fetcher(url))
        - Обычно в качестве аргумента fetch передают url или строковую переменную