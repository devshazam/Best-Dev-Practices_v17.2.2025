Создание массива
        let x1 x1 = []
        let x1 = new Array("Saab", "Volvo", "BMW");

Заполнение массива элементами
        let x1 = []
        x1[1] = 2 
        console.log(x1) // return [2]

In
        console.log(0 in array) // вернет boolean если в массиве есть свойство с позицией 0

at()
        let res = ['a', 'b', 'c'].at(-1);
        console.log(res);

Array(5)
Array.apply(null, Array(5)).map(function () {})
Array.from('abcde')
	return Array.from(Array(n), (_,i)=>++i)
Array(n).fill(0)
new Array(3)

# Методы
### delete()
	let x = [1, 'd']; 
	delete x[0];
		x => [undefined, 'd']

### Array.isArray()
	let x = Array.isArray([1,2,3,4]);
		x => true
### map()
	let x1 = [65, 44, 12, 4].map((elem, index) => { return elem * 10 })
		x1 => [650, 440, 120, 40]

### forEach() -> return void
        ⛔break не работвает!
        ⛔return не работвает!
        let arr = [1, 2, 3, 4, 5];
        arr.forEach((elem) => {console.log(elem);});

### reduce() -> return DIFFERENT NEW VALUE
        let numbers = [175, 50, 25];
        let NEW = numbers.reduce((total, num) => total - num, 0); // return 100

find() -> return NEW ELEMENT
        Найдет первое совпадение в массиве согласно колбеку:
        let res = arr.find(function(currentValue) { return currentValue > 0; });
        console.log(res) // return 1

sort() -> return MODIFIED SAME ARRAY
        Сортирует массив по умолчанию .sort() если массив начинается с 1 - иначе:
        var array = [140000, 104, 99];
        array.sort((a, b) =>  a - b); // сортировка массива цифр по порядку

every() -> return BOOLEAN
        все елементы должны удовлетворять условию ф-ции =>(true/false)
        let ages = [32, 33, 16, 40];
        ages.every(age => age > 18) // return false

filter() -> return DIFFERENT NEW VALUE
        // вернет массив только с елементами прошедшими тест
        let ages = [32, 33, 16, 40];
        let x1 = ages.filter(age => age >= 18); // x1 -> [32, 33, 40]

indexOf() -> return NUMBER(index | -1)
        let fruits = ["Banana", "Orange", "Apple", "Mango"];
        let index = fruits.indexOf("Apple"); // return 2
        
массив.findIndex(функция);






        (start, end) -> return DIFFERENT NEW VALUE
        // вернет массив элементов от start до end
        let arr = ['a', 'b', 'c', 'd', 'e'];
        let sub = arr.slice(1);
        console.log(sub);
splice(start, end) -> return DIFFERENT NEW VALUE
        // вернет массив элементов от start до end
        let fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
        let citrus = fruits.slice(1, 3); // return ['Orange', 'Lemon']




includes() -> return  BOOLEAN
        array.includes("Mango"); // если array содержит "Mango", то вернет true

push() -> return MODIFIED SAME ARRAY
        // добавляет елемент в конец массива, оставив остальные члены на своих позициях
        let arr = ['a', 'b', 'c', 'd'];
        let x1 = arr.push('e');
        arr // return ['a', 'b', 'c', 'd', 'e']
pop() -> return MODIFIED SAME ARRAY
                // удалит последний элемент массива, оставив остальные члены на своих позициях
                let arr = ['a', 'b', 'c', 'd', 'e'];
                let x1 = arr.pop();
                arr // return ['a', 'b', 'c', 'd']
                x1 // return 'e'

shift() -> return MODIFIED SAME ARRAY
        // удаляет первый элемент из массива
unshift() -> return MODIFIED SAME ARRAY
        let arr = ['a', 'b', 'c', 'd', 'e'];
        arr.unshift('1', '2');
        console.log(arr); // return 








function longestSlideDown (pyramid) {

  let x1 = R(pyramid, [pyramid[0]], 1)
  console.log(x1)
  let f = Math.max(...x1)
//   console.log(f)
  return f
  
}


function R(pyramid, arr, n){
  if(pyramid[n]){
    
    let x1 = Array(n + 1).fill([])
	console.log(x1, 2)
    for(let z in arr){
      
        for(let x in arr[z]){
            x1[z] = [...x1[z], arr[z][x] + pyramid[n][+x]];
            x1[+z + 1] = [...x1[+z + 1], arr[z][x] + pyramid[n][+x + 1]];            
        }

    }
//       console.log(x1)
    return R(pyramid, x1, +n + 1)
  }else{
    return arr
  }
}