# ES6 style
    export let x1 = 1;
        import { x1 } from './Test';

        import * as objectName from  './Test';
            objectName.methodeName

    export default function getName(){}
        import varName from './Test.js'; // имя импрота (varName) не имеет значение


# COMMON style
        module.exports = math;
            const math = require('./math'); // импортирует объект math
        
        module.exports = {square, cube};
            const {square, cube} = require('./math'); // деструктуризация объекта


# Re-export
	> export * from '@/x-config/x1-banner';
	⛔нельзя использовать в Nextjs - https://nextjs.org/docs/messages/export-all-in-page