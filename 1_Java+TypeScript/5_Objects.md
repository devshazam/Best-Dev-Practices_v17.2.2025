
METHODS ##################################################################################

let obj = { 0: 'a', 1: 'b', 2: 'c' };
console.log(Object.keys(obj)); //  ['0', '1', '2']
console.log(Object.values(obj)); // ['a', 'b', 'c']
console.log(Object.entries(obj)); // [ ['0', 'a'], ['1', 'b'], ['2', 'c'] ]
    const arr = [
  ["0", "a"],
  ["1", "b"],
  ["2", "c"],
];
const obj = Object.fromEntries(arr);
let newObj = Object.assign({}, obj); // копирование объекта



OBJECTS =============================================


// ForIn 
    const person = {fname:"John", lname:"Doe", age:25};
    let tXt = "";
    for (let x in person) {
        txt += person[x] + " ";
    } // return "John Doe 25 "


```js
{
  "array": [
    1,
    2,
    3
  ],
  "boolean": true,
  "color": "gold",
  "null": null,
  "number": 123,
  "object": {
    "a": "b",
    "c": "d"
  },
  "string": infinity
}