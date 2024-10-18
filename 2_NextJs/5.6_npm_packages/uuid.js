// Install
// $ npm i uuid

// ########## USE = 2 steps ##############
// any place within app
import { v4 as uuidv4 } from 'uuid'; // 1/2 step - import 
uuidv4(); // 2/2 step - use ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'




// Common.js style
const { v4: uuidv4 } = require('uuid'); // 1/2 step - import 
uuidv4(); // 2/2 step - use ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'