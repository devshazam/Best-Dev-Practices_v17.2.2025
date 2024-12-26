# Проеобразование из объекта
  let obj = { 0: 'a', 1: 'b', 2: 'c' };
    Object.keys(obj); =>  ['0', '1', '2']
    Object.values(obj); => ['a', 'b', 'c']
    Object.entries(obj); => [ ['0', 'a'], ['1', 'b'], ['2', 'c'] ]

# Преобразование в объект
  const obj = Object.fromEntries(arr); // преобразование двумерного массива в объект
    - [["0", "a"], ["1", "b"]] => {"0":"a", "1":"b"}
  let newObj = Object.assign({}, obj); // копирование объекта

# Удалить свойство из объекта
    const {descriptionCard, ...secondObject } = cardData;

# Деструктуризация объекта - массива
	const [a, b, ...{ length }] = [1, 2, 3, 3]; // с помощью rest мы получаем массив [3,3] - и он же является объектом со свойством length - которое равно 2

kopi34.ruluristy.ru
taxi-cities.ru
https://t.me/kopi34_bot
rus1transfer.ru
davse.ru

legenda-dom.ru
	- ⚡<a href="https://" target="_blank">kopi34.ru</a> (Web-store_Calcuator: react, postgreSQl, prisma);
- ⚡<a href="https:///" target="_blank">taxi-cities.ru</a> (SEO-Lending: nextjs14);
- ⚡<a href="" target="_blank">@kopi34_bot</a> (telegram-bot: django, nextjs)
- <a href="https:///" target="_blank">luristy.ru</a> (Lending: nextjs);

- <a href="https://seo-cy.ru" target="_blank">seo-cy.ru</a> (Lending: nextjs static);
- <a href="https://" target="_blank">rus1transfer.ru</a> (Lending: Stack: react);
- ⚡<a href="https://" target="_blank">davse.ru</a> (App: nextjs, prisma);
- <a href="https://" target="_blank">legenda-dom.ru</a> (Lending: Stack: react, redux);
- ...
- 6 real cool web-stores:
- <a href="https://uniformaonline.ru" target="_blank">uniformaonline.ru</a> (Web-store: react, postgreSQl, prisma);
- <a href="https://dostupsreda.ru" target="_blank">dostupsreda.ru</a> (Web-store: react, redux);
- <a href="https://re.kufar.by" target="_blank">re.kufar.by</a> (Web-store: react, mongoDB, sequalize, Elasticsearch);
- <a href="https://patterneasy.com" target="_blank">patterneasy.com</a> (Web-store-simple);
- <a href="https://flacon-magazine.com" target="_blank">flacon-magazine.com</a> (Web-store-simple);