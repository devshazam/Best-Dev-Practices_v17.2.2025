- findUnique(): object | null - поиск по уникальному значению (id, email)
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
- 
