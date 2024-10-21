## Desc = https://blog.designly.biz/next-js-14-data-fetching-paradigms-client-vs-servers
    - SWR нужен для работы на клиенте (на сервере не работает!)
    - Работает с Server Action - вызывает напрямую импортированную ф-цию из директории `@lib/...`

## Quickstart:
    1_ `const { data: songs, isLoading, isValidating, mutate } = useSwr('songs', fetchSongs);`
        ГДЕ:
            - data = полученая асинхронная информация