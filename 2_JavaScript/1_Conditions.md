# Conditions 
    - Nested conditional
		if((1 > 2 || 1 > 2) && (1 > 2 || 1 > 2))
    - Условное присвоение
		let a = varOne || 6;
	- Перемена значений ф-ций
		[firstName, lastName] = [lastName, firstName];
# Conditional chains
	⛔Важно: разветвление должны идти в правую сторону 
	function example() {
	return condition1 ? value1
		: condition2 ? value2
		: value3;
	}

	n * (n % 2 ? 9 : 8);

# Falsy = 6 
	false, 0, '', null, indefined, NaN

# Check:
## Only null and undefined
	if(variable == null)
## is Number ?
	Number.isInteger(123);
    isNaN('we') // проверка на число
## Array 
	letters instanceof Array // 
	Array.isArray() 
	array.length


