

https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries#connect-or-create-a-record
const result = await prisma.post.create({
  data: {
    title: 'How to make croissants',
    author: {
      connectOrCreate: {
        where: {
          email: 'viola@prisma.io',
        },
        create: {
          email: 'viola@prisma.io',
          name: 'Viola',
        },
      },
    },
  },
  include: {
    author: true,
  },
})