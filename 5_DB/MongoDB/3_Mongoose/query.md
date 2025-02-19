```js

// CREATE:
    1:
        const awesome_instance = new SomeModel({ name: "awesome" });
        await awesome_instance.save();

    2: 
        const awesome_instance = new SomeModel(); // or find instance
        awesome_instance.name = "New cool name";
        await awesome_instance.save();
    
    3:
        await SomeModel.create({ name: "also_awesome" });

// FIND:
    1:
        await Model.findById(id, 'name length').exec(); // WHERE id: id SELECT name & length

    2: 
        await Model.findOne({ country: 'Croatia' }, 'name length').exec(); // WHERE country: Croatia SELECT name & length
    
    3:
        await Model.find()
                .where("sport").equals("Tennis") // WHERE sport: Tennis 
                .where("age").gt(17).lt(50) // Additional where query
                .where('likes').in(['vaporizing', 'talking'])
                .skip(100).limit(20) // skip тоже самое что offset
                .sort({ age: -1 })
                .select("name age")
                .exec();
        
        await DiscoModelunt.findById(id)
            .select("name age")
            .populate('userId', 'name phone')
            .exec();


            https://stackoverflow.com/questions/26691543/return-certain-fields-with-populate-from-mongoose
            .find(query).select({'advtId': 0})
            .populate({
                path: 'influId',
                model: 'influencer',
                select: { '_id': 1,'user':1},
                populate: {
                    path: 'userid',
                    model: 'User'
                }
            })
            .populate('campaignId',{'campaignTitle':1})
            .exec(callback);

// DELETE:
    deleteOne() and deleteMany()
        await Tank.deleteOne({ size: 'large' }); // return { acknowledged: true, deletedCount: 1 }
            // OR
            Tank.find({ id:333 }).remove().exec(); // под вопросом!?


// UPDATE: 
    await Tank.updateOne({ size: 'large' }, { name: 'T-90' });


// COUNT:
    1: 

