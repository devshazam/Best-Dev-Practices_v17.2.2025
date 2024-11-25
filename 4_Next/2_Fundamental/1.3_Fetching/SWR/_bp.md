# SWR
	- intro:
		- swr для работы c ServerAction
		- ⚠️кеширует все запросы по умолчанию по ключу!
			- ⚠️Если у двух запросов будет один ключ - то мы получим один ответ!

# Definition
	- Условная выборка: это выборка запрос которой зависит от значения аргумента key, если аргумент равен null или ф-ция возвращает false, error
		- https://swr.vercel.app/ru/docs/conditional-fetching
	- Ревалидация: это перезагрузка данных минуя кеш - это нужно для обновления данных после внесения изменений (например в БД)
	- Мутация: это ручная ревалидация данных 

# bp:
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


