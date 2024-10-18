# 1 Naming Convention:
    - 
  
- Концепции языка TypeScript
    - Тип переменным задается явно (самостоятельно) и автоматически при объявлении
    - Тип нужно объявлять для переменных , ф-ций, цикла for

- Best_Practices:
    - Именование в camelCase
        - Переменные (описание существа): arrayOfDevices
        - Функции (описание деействия): sendMessage
        

- строки, числа и boolean не изменяемы, а массивы и объекты изменяемы
    - 
- 
- as - переопределяет тип любой переменной
    -   let x2:string = morseCode.split('   ').map((x:string) => {
            console.log(x.split(' '))
            let x3 = x.split(' ')
            return x3.map((z2:any) => x1[z2 as keyof typeof x1]).join('')
            }).join(' ')
        console.log(x2)
        return x2

- Loops 
    for (let x; x <= 3; x++) { ... } // 

    while (x < 10){ ... } // 

    NOT USAGE: из-за автоопределения циклы возвращают разный x (String and Number)
        for (let x in var){ ... } // FOR_INDEX - loop index of String, Array, Object
            x return STRING !!!
        for (let x of var){ ... } // FOR_VALUE - loop value of String, Array 


_1
    let a = varOne || 6; // если varOne не существует, то будет 6, НО varOne должно быть задано undefined 

_1:
    setTimeout(function() {alert('!'); }, 3000); 
    
_3:
    Spred - разбить массив (объект) на елементы
        - func(...[1, 2, 3, 4, 5]); //! func(1,2,3,4,5);
        - const newObject = {...oneObject, ...twoObject};
        
_4:
    Rest
        - func(a, b, ...rest);
        - const [one, two, ...rest] = oneArray;

- деструктуризация 
    - Массивы
        - const [one, two] = oneArray // в пременные one и two запишутся первые два елемента массива
        - const [, , one, two] = oneArray // в пременные one и two запишутся 3 и 4 елементы массива
        - const [one, two, ...rest] = oneArray // в пременные one и two запишутся первые два елемента массива, а остальные в переменную rest
        - x12[x5[1]] = [x5[0], ...(x12[x5[1]] ? x12[x5[1]] : [])]

    - Объекты
        - const {one, two} = oneObject // переменные только под темиже
        - const {one, two, outside} = oneObject // если имени outside нет в объекте, то outside = undefined
        - const {one: two} = oneObject // alias - меняет имя переменной при деструктуризации
        - x12[x5[1]] = [x5[0], ...(x12[x5[1]] ? x12[x5[1]] : {})]
        const nextConfig = {
                assetPrefix: isDev ? undefined : 'https://cdn.mydomain.com',
            }
        
        
- JSON// https://www.w3schools.com/js/js_json_intro.asp
    var myJSON = JSON.stringify(myObj); // --> json
    var obj = JSON.parse('{"firstName":"John", "lastName":"Doe"}');

Check_type
    Array 
        letters instanceof Array // 
        Array.isArray() 
        array.length

    Number
        isNaN('we') // проверка на число
        Number.isInteger(+width) // проверка на целое число

    Object
        Object.keys(devices).length // Проверка массива на пустоту 

UNICODE
    - let text = "HELLO WORLD";
        let code = text.charCodeAt(0); // return 72 из таблицы Юникода
    - let char = String.fromCharCode(65); // вернет символ по его цифре юникода