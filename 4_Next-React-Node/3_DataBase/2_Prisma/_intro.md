# 
	- Отношения
		- include
	- Count ana find many
		const [posts, totalPosts] = await prisma.$transaction([
			prisma.post.findMany({ where: { title: { contains: 'prisma' } } }),
			prisma.post.count(),
		])