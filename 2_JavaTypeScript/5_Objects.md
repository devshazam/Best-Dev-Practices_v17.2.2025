# Проеобразование из объекта
  let obj = { 0: 'a', 1: 'b', 2: 'c' };
    Object.keys(obj); =>  ['0', '1', '2']
    Object.values(obj); => ['a', 'b', 'c']
    Object.entries(obj); => [ ['0', 'a'], ['1', 'b'], ['2', 'c'] ]

# Преобразование в объект
  const obj = Object.fromEntries(arr); // преобразование двумерного массива в объект
    - [["0", "a"], ["1", "b"]] => {"0":"a", "1":"b"}
  let newObj = Object.assign({}, obj); // копирование объекта
