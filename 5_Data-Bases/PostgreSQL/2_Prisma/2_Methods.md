#

    > await prisma.user.findMany() // получить всех пользователей
    - Поиск по уникальному значению:
    	> findUnique(where: { email: 'test@prisma.io' })

>     	> {id: 1, email: ...} | null

    - get or create:
    	const upsertUser = await prisma.user.upsert({
    		where: {
    			email: 'test@prisma.io',
    		},
    		update: {},
    		create: {
    			email: 'test@prisma.io',
    			name: 'Test User',
    		},
    	})

>     	> {id: 1, email: ...} | null

    - Count ana find many
    	const [posts, totalPosts] = await prisma.$transaction([
    		prisma.post.findMany({ where: { title: { contains: 'prisma' } } }),
    		prisma.post.count(),
    	])
    - updateMany() // найти  все записи с заданным параметром поиска и изменить все заданные поля
