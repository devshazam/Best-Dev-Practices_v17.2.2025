

## Деструктуризация
    - Объекты
        - const {one, two} = oneObject // переменные только под темиже
        - const {one, two, outside} = oneObject // если имени outside нет в объекте, то outside = undefined
        - const {one: two} = oneObject // alias - меняет имя переменной при деструктуризации
        - const {name, age, ...contacts} = tom;
        - let display = ({firstName, lastName}) => console.log(`${firstName} ${lastName}`);
        
    - Строки
        - const [ ...rest ] = 'qwerty'; // rest = ['q','w','e','r','t','y']
        - let x1 = 'qwerty'; 
            [ ...x1 ] // => ['q','w','e','r','t','y']

    - Массивы
        - const [one, two] = oneArray // в пременные one и two запишутся первые два елемента массива
        - const [, , one, two] = oneArray // в пременные one и two запишутся 3 и 4 елементы массива
        - const [one, two, ...rest] = oneArray // в пременные one и two запишутся первые два елемента массива, а остальные в переменную rest
        - const fruits = ["Bananas", "Oranges", "Apples", "Mangos"];
            - let {[0]:fruit1 ,[1]:fruit2} = fruits; // вызов конкретных переменных
        - let firstName = "John", lastName = "Doe";
            - [firstName, lastName] = [lastName, firstName]; // поменять значения переменных между ними.

## JSON
    let myJson = JSON.stringify(myObject);
    let myObject = JSON.parse(myJson);


## UNICODE
    - let code = "HELLO".charCodeAt(0); // return 72 первая буква 'H' из таблицы Юникода 
    - let char = String.fromCharCode(65); // вернет символ по его цифре юникода


## нахождение промежутка
        - const X_2 = [[0, 1], [1, 5], [5, 10], [10, 50], [50, 100], [100, 500], [500, Infinity]].findIndex((elem) => X_1 >= elem[0] && X_1 < elem[1])

## конвертироватьстроковый символ в бинарную строку
        - var a = 'a'.charCodeAt(0).toString(2); 

## удалить все дубли из массива
        - let uniqueArray = x1.filter(function(item, pos) { return x1.indexOf(item) == pos; })

## Поменять значения переменных местами если одно больше другого
        if(x2.length > x1.length) [x1, x2] = [x2, x1];

## Codewar
         let x1 = 0
        for( let x = 0; x < arr.length; x++){
                if(){
                }else{
                }
        }

# Строки
	- string.charAt(0).toUpperCase() + string.slice(1)


# Next prime
	function nextPrime(previousPrime) {
    let value = previousPrime;
    if (value > 2) {
        var i, q;
        do {
            i = 3;
            value += 2;
            q = Math.floor(Math.sqrt(value));
            while (i <= q && value % i) {
                i += 2;
            }
        } while (i <= q);
        return value;
    }
    return value === 2 ? 3 : 2;
}