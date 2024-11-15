# Создание многих записей:
- https://www.prisma.io/docs/orm/reference/prisma-client-reference#select
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
	// Сортировка:
	orderBy: { role: 'desc', },							// Сортировка по 1 параметру
	orderBy: [{ role: 'desc', },{ name: 'asc', }]		// Сортировка по нескольким параметрам
	// Пагинация:
	skip: 10,   // пропустить первые 10
  	take: 5,    // Взять в кол-ве 5
    })
    - 
```

## READ:
### findUnique()
    const user = await prisma.user.findUnique({
        where: {
            email: 'elsa@prisma.io',
        },
    })
### findFirst()