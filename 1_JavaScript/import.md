```js

// COMMON (NPM_OLD)
    const math = require('./math'); // импортирует объект math
        const {square, cube} = require('./math'); // деструктуризация объекта

        // ===========================>

        module.exports = math;
        module.exports = {square, cube};



// JS_ES6 ================================================================================================
        import {varName1, varName2} from './Test.js'; // можно импортировать только те елементы которые нужны.
            import * as test from  './Test.js'; // импортирует объект test, c елементами varName1, varName2
        // Import default:
            import varName from './Test.js'; // имя импрота (varName) не имеет значение

        // ===========================>

        // befor
        export let m1 = ...
        export function funName
        // after
        export {m1, funName, ClassName}; //
        // evport default:
            // befor
            export default let m1...
            export default function...
            // after
            export default <varName>;
    