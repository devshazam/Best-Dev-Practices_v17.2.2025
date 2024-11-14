# Создание многих записей:
    - createMany vs createManyAndReturn
```js
    const result = await prisma.user.findMany({
    where: {
        // Либо Либо
        OR: [
            { 
                email: 
                { 
                    endsWith: 'prisma.io', // почта оканчивается на ... 
                    mode: 'insensitive', // Не учитывать заглавные буквы
                }, 
             }, 
            { email: { startsWith: '_benny' } }, // почта начинается с ...
        ],
        NOT: {
        email: {
            endsWith: 'hotmail.com',
        },
        },

        // Те записи где значения пусты (обычно по умолчанию)
        content: null,
        content: { not: null },
    },
    select: {
        email: true,
    },
    })
    - 
## READ:
### findUnique()
    const user = await prisma.user.findUnique({
        where: {
            email: 'elsa@prisma.io',
        },
    })
### findFirst()