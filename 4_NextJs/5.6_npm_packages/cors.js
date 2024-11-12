// Install
// $ npm install cors

// ########## USE = 2 steps ##############
// index.js
var express = require('express')
var cors = require('cors') // 1/2 step - import
var app = express()

app.use(cors()) // 2/2 step - set up as middle

app.get('/products/:id', function (req, res, next) {
  res.json({msg: 'This is CORS-enabled for all origins!'})
})

app.listen(80, function () {
  console.log('CORS-enabled web server listening on port 80')
})