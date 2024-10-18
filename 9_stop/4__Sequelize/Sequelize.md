```js

https://my-js.org/docs/guide/sequelize/#%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%8D%D0%BA%D0%B7%D0%B5%D0%BC%D0%BF%D0%BB%D1%8F%D1%80%D0%BE%D0%B2-%D1%81-%D0%B0%D1%81%D1%81%D0%BE%D1%86%D0%B8%D0%B0%D1%86%D0%B8%D1%8F%D0%BC%D0%B8


MAIN =============================================================

Create:
    const jane = await User.create({ firstName: "Jane", lastName: "Doe" }); // 
        return object // если создался
        1. В строки можно записывать пустые строки

    const captains = await Captain.bulkCreate([ // массовое создание
    { name: 'Jack Sparrow' },
    { name: 'Davy Jones' }
    ]);


Upsdate:
    await User.update({ lastName: "Doe" }, {where: {id : "1"}}); //
        array [0] // если не нашел кого изменять
        array [1] // если нашел кого изменять


Find:
    const { count, rows }  = await Device.findAndCountAll({where: {id : "1"}, order: [['createdAt', 'DESC']], limit, offset});


    const user = await ModelName.findAll();
        return [] // если нет таких
        where: { id: [1,2,3] } // найдет массив объектов по их ID из масиива
        attributes: ['id', 'price', 'price_img'] // возьмет только конкретные поля
        

    const user = await ModelName.findOne({where: {id : "1"}});
        return null // if not found 

Destroy:
    await User.destroy({where: {id : "1"}}); // return 1 если успешно и 0 если нет
        return 1 // number если удалился
        return 0 // number если не удалился



ASSOCIATION ============================================================


Destroy:
    const row = await City.findOne({where: { cityName: "Glasgow" }});
    await row.destroy(); // deletes the row --- return [] (empty array)

Update:
    const row = await City.findOne({where: { cityName: "Glasgow" }});
    jane.set({ name: "Ada", favoriteColor: "blue" });
    await jane.save(); // 

User.hasOne(device)
    const row = await User.findOne({where: { id }});
    await row.getDevice(); // получает одного юзера - если нет, то null
        const row = await Device.findOne({where: { id }});
        await row.getUser(); // получает связанного  юзера - если нет, то null

User.hasMany(device)
    const row = await User.findOne({where: { id }});
    await row.getDevices(); // получает все девайсы - если нет, то []
    await row.countDevices(); // посчитает кол-во девайсов связанных с юзером 
        const row = await Device.findOne({where: { id }});
        await row.getUser(); // получает связанного  юзера - если нет, то null



========================== Transaction ==================================
https://www.ultimateakash.com/blog-details/IiwzPGAKYAo=/How-to-implement-Transactions-in-Sequelize-&-Node.Js-(Express)

Пример: DeviceController --> deleteItemFromBasket



Math ==============================================================

await User.count({where: {id: 1}}); // rerurn count of item

await User.increment({age: 5}, { where: { id: 1 } }) // Will increase age to 15
await User.increment({age: -5}, { where: { id: 1 } })

await User.max('age'); // 40
await User.max('age', { where: { age: { [Op.lt]: 20 } } }); // 10
await User.min('age'); // 5
await User.min('age', { where: { age: { [Op.gt]: 5 } } }); // 10
await User.sum('age'); // 55


============================================================


type: DataTypes.INTEGER // INTEGER and STRING are two main types
primaryKey: true // only for id field
autoIncrement: true // only for id field + auto add new value
unique: true // for unique value for this field
defaultValue: 'green' // it's default value - if you did't inset value
validate: {is: /^[0-9a-f]{64}$/i} // compare with regular extension
allowNull: false // (не обязательное поле) разрешно не заполнять при создании или изменении


