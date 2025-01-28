- Концепции языка TypeScript
    - Тип переменным задается явно (самостоятельно) и автоматически при объявлении
    - Тип нужно объявлять для переменных , ф-ций, цикла for



# Удалить свойство из типа
    type ExcludedType = ExcludeProps<FullType, 'prop2'>;
    - https://www.geeksforgeeks.org/how-to-exclude-property-from-type-in-typescript/
	- Удалить  null и undefined 
		- In TypeScript, a postfix ! removes null and undefined


# as - переопределяет тип любой переменной
    -   x1[z2 as keyof typeof x1]


if (files[x] instanceof File) {
		const extension = (files[x] as File).type.split('/')[1];
}

# 	Проверка объекта на принадлежность к классу
	obj instanceof Class

# Глобальные классы: 
	- class File - 
	- class Error - класс 