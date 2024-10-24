
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
