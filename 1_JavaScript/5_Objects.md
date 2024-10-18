let obj = { 0: 'a', 1: 'b', 2: 'c' };
In
        console.log(0 in array) // вернет boolean если в массиве есть свойство с позицией 0

Array_Creating
        let x1 x1 = []
        let x1 = new Array("Saab", "Volvo", "BMW");

Заполнение массива элементами
        let x1 x1 = []
        x1[1] = 2 
        console.log(x1) // return [undefind, 2]

METHODS ##################################################################################

let obj = { 0: 'a', 1: 'b', 2: 'c' };
console.log(Object.keys(obj)); //  ['0', '1', '2']
console.log(Object.values(obj)); // ['a', 'b', 'c']
console.log(Object.entries(obj)); // [ ['0', 'a'], ['1', 'b'], ['2', 'c'] ]








OBJECTS =============================================


// ForIn 
    const person = {fname:"John", lname:"Doe", age:25};
    let tXt = "";
    for (let x in person) {
        txt += person[x] + " ";
    } // return "John Doe 25 "
