lst = ['a', 'b', 'c']
for item in enumerate(lst): # получение значения и ключа в цикле
	key, value = item
	print(key)
	print(value)
	print()
	
for key in dct:
	print(key)
	
for num in range(1, 10):
	print(num) # выведет 1, 2... 9