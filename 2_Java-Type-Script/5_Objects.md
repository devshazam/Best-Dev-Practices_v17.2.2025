# Проеобразование из объекта
  let obj = { 0: 'a', 1: 'b', 2: 'c' };
    Object.keys(obj); =>  ['0', '1', '2']
    Object.values(obj); => ['a', 'b', 'c']
    Object.entries(obj); => [ ['0', 'a'], ['1', 'b'], ['2', 'c'] ]

# Преобразование в объект
  const obj = Object.fromEntries(arr); // преобразование двумерного массива в объект
    - [["0", "a"], ["1", "b"]] => {"0":"a", "1":"b"}
  let newObj = Object.assign({}, obj); // копирование объекта

# Удалить свойство из объекта
    const {descriptionCard, ...secondObject } = cardData;

# Деструктуризация объекта - массива
	const [a, b, ...{ length }] = [1, 2, 3, 3]; // с помощью rest мы получаем массив [3,3] - и он же является объектом со свойством length - которое равно 2

