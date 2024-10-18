```js
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/mongoose
- Установка графического интерфейса MongoDB Compass Download (GUI) - https://www.mongodb.com/try/download/compass
- Установка - https://www.mongodb.com/docs/manual/installation/
    - Загрузка версии Community - https://www.mongodb.com/try/download/community
- подключение и простой роутинг - https://dev.to/franciscomendes10866/setup-mongodb-with-mongoose-and-express-4c58



=======================================================
https://mongoosejs.com/docs/schematypes.html
MONGOOSE: - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/mongoose

Type:
    common:
                                    required: true, // reference to the 
                                            required: [true, "Why no eggs?"], // возможно  
                                    default: Date.now //
                                            default: "01/01/23" //
                                    alias: 'a'  //
                                    get: v => Math.round(v), // можно добавить геттер - он будет срабатывать при попытке получить  значение
                                    set: v => Math.round(v), // можно добавить сеттер - он будет срабатывать при попытке записать  значение

    name_one: { type: string, required: true, } // 
                                    enum: ["Coffee", "Tea", "Water"], // значение должно быть равно одному из значений перечисления
                                    
                                    
                                    index: true
                                    unique: true // возможно??
    age: { type: Number,  },
                                    min: 18, 
                                    max: 65, 
    current_date: { type: Date, default: Date.now() }// тип дата и по умолчанию уствнавливается текущая дата

    mixed: Schema.Types.Mixed, // любые типы данных

    book: { type: Schema.Types.ObjectId, ref: "Athor" } // создание связи с автором



, { timestamps: true }
 { autoCreate: false, autoIndex: false });    


 