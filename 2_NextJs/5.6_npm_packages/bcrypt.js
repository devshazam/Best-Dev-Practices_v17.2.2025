// Install
// $ npm install bcrypt

// ########## USE = 3 steps ##############
// userController.js
const bcrypt = require('bcrypt')  // 1/3 step - import 

// 2/3 - хешиовать пароль 5 раз
const hashPassword = await bcrypt.hash(password, 5)



// 3/3 - расхешировать праоль и сравнить с текушим
let comparePassword = bcrypt.compareSync(password, user.password)