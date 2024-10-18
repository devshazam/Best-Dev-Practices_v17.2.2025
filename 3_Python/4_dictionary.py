dictionary.pop("key", None) # удалить по ключу если есть

dct1.update(dct2) # объединяет два словаря
print(dct1) # выведет {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'f': 5}

del dct['a'] # удаление элемента по ключу

dct.pop('a') # удаление элемента по ключу
dct.popitem() # удаляет последний элемент


print('a' in dct) # выведет True
print('a' not in dct) # выведет False

print(dct.get('x', 4)) # если элемента нет - выведет 4

res = dct.keys() # получение ключей

res = dct.values() # получение значений

res = dct.items()   # получение пар ключ-значение