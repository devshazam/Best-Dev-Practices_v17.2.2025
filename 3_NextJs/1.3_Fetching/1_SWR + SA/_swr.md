```js
	const { data, isLoading, mutate, isValidating } = useSWR(key, fetcher)

	// ГДЕ:
	// 	- data - информация 
	// 	- isValidating - статус ревалидации
	// 	- mutate - ф-ция ревалидации
	// 	- ⛔isLoading - статус загрузки - вместо лучше использховать 
	// 		- isValidating
	// 		- !data.error
	// 	- ⛔error - ошибка ⛔Не работает с обычным try{}catch{}

	// 	- key - ключ кеширования
	// 	- ⚠️Если у двух запросов будет один ключ - то мы получим один ответ!


import { useSWRConfig } from "swr"

export default function Testing(){

	const { data: orderList, isValidating, mutate } = useSWR(user?.sub ? ['/api/user/get-orders', user.id] : null, ([url, id]) => getTenOrdersById(url, id))


	if (!data) {
		return <p>Loading...</p>;
	}

	if (data.error) {
		return <p>Ошибка загрузки!</p>;
	}

	return (
		<p>{data}</p>
	);
}




