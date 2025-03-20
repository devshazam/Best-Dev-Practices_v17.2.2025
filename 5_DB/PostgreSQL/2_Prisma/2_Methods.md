#
> findMany - найти много
    	- await prisma.user.findMany(where: { email: 'test@prisma.io' }) // получить всех пользователей
	RETURN [{id: 1, email: ...}...] | []

> findUnique - найти уникального
	- await prisma.user.findUnique(where: { id })
	RETURN {id: 1, email: ...}| null

> findFirst()

> upsert - найти или создать
    	- await prisma.user.upsert({
    		where: { email: 'test@prisma.io', },
    		update: { name: 'Test User' }, // обновить
    		create: { email: 'test@prisma.io', name: 'Test User' } // создать
    	})
	RETURN {id: 1, email: ...} | null

> Count ana find many
    	const [posts, totalPosts] = await prisma.$transaction([
    		prisma.post.findMany({ where: { title: { contains: 'prisma' } } }),
    		prisma.post.count(),
    	])

> updateMany() // найти  все записи с заданным параметром поиска и изменить все заданные поля

> count - return number | 0

