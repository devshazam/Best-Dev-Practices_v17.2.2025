# SWR
	- swr для работы c ServerAction
    - SWR работает только в клиентских компонентах!
	- ⚠️кеширует все запросы по умолчанию по ключу!
		- ⚠️Если у двух запросов будет один ключ - то мы получим один ответ!
## Fetch:
- quickstart:
	```js
		const { data: orderList, error } = useSWR(() => (user && user.sub) ? ['/api/user/get-orders', user.sub] : null, ([url, id]) => getTenOrdersById(url, id))
	```
		- ref:
			- Аргументы: https://swr.vercel.app/ru/docs/arguments
			- Условное исполнение: https://swr.vercel.app/ru/docs/conditional-fetching
        - key - ключ кеширования ⚠️должен быть уникален для разных запросов, иначе будет возвращать одинаковый ответ
        	- Обычно в качестве ключа передают url + get параметры
		- Состояния переменных: [в процессе, инфо. получена, ошибка]
        	- data -> [undefined, data, undefined]
   	    	- error -> [undefined, undefined, error]
        	- isLoading -> [true, false, false]


