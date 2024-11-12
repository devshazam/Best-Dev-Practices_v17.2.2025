```js
// Install
// $ npm install jsonwebtoken

// ########## server ##############
const jwt = require('jsonwebtoken')


// 2 - проверить секретный ключ
const token = req.headers.authorization.split(' ')[1] // Bearer asfasnfkajsfnjk
const decoded = jwt.verify(token, process.env.SECRET_KEY)

// 3
const generateJwt = (id, email, role) => {
    return jwt.sign(
        {id, email, role},
        process.env.SECRET_KEY,
        {expiresIn: '24h'}
    )
}
const token = generateJwt(user.id, user.email, user.role)
return res.json({token})


// ########## client ##############

npm install jwt-decode

// 2 step
var token = "eyJ0eXAiO.../// jwt token";
var decoded = jwt_decode(token);
 
console.log(decoded);
 
/* prints:
 * { foo: "bar",
 *   exp: 1393286893,
 *   iat: 1393268893  }
 */
