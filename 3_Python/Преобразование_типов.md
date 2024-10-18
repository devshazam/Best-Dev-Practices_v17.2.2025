- List
    In [7]: list("string")
    Out[7]: ['s', 't', 'r', 'i', 'n', 'g']

    In [8]: list({1, 2, 3})
    Out[8]: [1, 2, 3]

    dct = { 'a': 1, 'b': 2, 'c': 3 } # Получим все его значения в виде списка:
    res = list(dct)
    print(res) # выведет ['a', 'b', 'c']


- String
    str()

Integer
    int()

Float
    float()

Dictionary
    lst = [['a', '1'], ['b', '2']]
    dct = dict(lst)
    print(dct) # выведет {'a': '1', 'b': '2'}