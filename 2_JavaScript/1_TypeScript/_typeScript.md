# Перезапись типов
	type Override<T1, T2> = Omit<T1, keyof T2> & T2;

	type AB = Override<A, { b: number }>
# as - переопределяет тип любой переменной
    -   x1[z2 as keyof typeof x1]


# 	Проверка объекта на принадлежность к классу
	obj instanceof Class
