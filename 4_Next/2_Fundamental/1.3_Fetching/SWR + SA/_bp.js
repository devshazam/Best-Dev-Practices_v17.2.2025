/* _intro:
	- swr для работы c ServerAction 
	- Basic USAGE:*/

	const { data, isLoading, mutate, error, isValidating } = useSWR(key, fetcher)

/*	_feature: 
		- key - ключ кеширования передают url + get параметры
			- ⚠️Если у двух запросов будет один ключ - то мы получим один ответ!
		- Переменные:
			- data -> [undefined, data, undefined]
			- error -> [undefined, undefined, error = {info: {message: "...", documentation_url: "..."}, status: 403}]
			- isLoading -> true во время получения данных при условии что первый запрос ещё не был выполнен
			- isValidating -> true каждый раз когда ревалидируются данные
			- mutate() -> заставляет основную ф-цию пере_запросить данные!
	
	_advanced:
		- Условная выборка: если аргумент key равен null или ф-ция возвращает false, error - то ф-ция не выполняется
		- Ревалидация: это перезагрузка данных минуя кеш - это нужно для обновления данных после внесения изменений (например в БД)
		- Мутация: это ручная ревалидация данных (onClick = {() => mutate()}) - это нужно для пере запроса данных после обновления данных в БД специально
*/

export default function UserButton(){

	const { data, isLoading } = useSWR(() => (user && user.sub) ? ['/api/user/get-orders', user.sub] : null, ([url, id]) => getTenOrdersById(url, id))
	/* Вариант 2 (облегченный):
	const { data: newName, isLoading, mutate } = useSwr('/api/', url => getPriceByName(url));
	*/

	if (isLoading) {
		return <p>Loading...</p>;
	}

	if (!data) {
		return <p>Ошибка загрузки!</p>;
	}

	return (
		<p>{data}</p>
	);
}




