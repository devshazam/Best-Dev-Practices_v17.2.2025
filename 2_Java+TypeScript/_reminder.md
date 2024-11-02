## Convert to other type
    - toBoolean
        !!string; // true
        Boolean(string); // true
    - toNumber
        ++string;
        Number(string);
    - toString
        `` + number;
        String(number);
## Loops 
    for (let x; x <= 3; x++) { ... } // 

    while (x < 10){ ... } // 

    NOT USAGE: из-за автоопределения циклы возвращают разный x (String and Number)
        for (let x in var){ ... } // FOR_INDEX - loop index of String, Array, Object
            x return STRING !!!
        for (let x of var){ ... } // FOR_VALUE - loop value of String, Array 


## Conditions 
    - if ( (e.ctrlKey || e.metaKey) && (e.key === 'Enter' || e.key === 'NumpadEnter') )
    - let a = varOne || 6; // если varOne не существует, то будет 6, НО varOne должно быть задано undefined 

## Timeout
    setTimeout(function() {alert('!'); }, 3000); 
    
        
## Rest
    Rest
        - func(a, b, ...rest);
        - const [one, two, ...rest] = oneArray;

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

## Check_type
    Array 
        letters instanceof Array // 
        Array.isArray() 
        array.length

    Number
        isNaN('we') // проверка на число
        Number.isInteger(+width) // проверка на целое число

    Object
        Object.keys(devices).length // Проверка массива на пустоту 

## UNICODE
    - let text = "HELLO WORLD";
        let code = text.charCodeAt(0); // return 72 из таблицы Юникода
    - let char = String.fromCharCode(65); // вернет символ по его цифре юникода