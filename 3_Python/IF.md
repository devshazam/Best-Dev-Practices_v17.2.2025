- in
    in
    not in

- and имеет приоритет над or
    if tst > 0 and tst < 5 or tst > 10 and tst < 20:
- or
    if (tst > 0 or tst < 5) and (tst > 10 or tst < 20)
- not 
    if not x > 1:

- !
    if f != 3:
- double
    if 2 < tst < 10:
- None
    if tst is None:
    if tst is not None:

Falsy: 0, None, False, '', [], {}, (),

match tst:
	case 'a':
		print('a')
	case 'b':
		print('b')
	case _:
		print('tst is unknown')


'сообщение, если условие 1 истинно' if условие 1 else 'сообщение, если условие 1 ложно'

isinstance(var, str) # dslftn True если 