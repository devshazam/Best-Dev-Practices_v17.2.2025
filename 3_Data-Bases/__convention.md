# Введение
	- Всегда использовать Transaction при использованиии боллее одного запроса с изменением
	- Структурировать БД прежде чем начинать строить в коде
		- 
	- Использовать отношения вместо изобретения костылей
		- Стараться не использовать отношения many-to-many - потому что во многих ORM нет достаточно инструментов для полноценной работы с ним
	- Типы данных соответствие к типовым данным
		- координаты - float
		- 
	Assosianions (отношения)
		- One_to_One - удобно использовать для свойств юнита, которые будут обрабатываться самостоятельно чтобы во второстепенной таблице это своиства были уникальными (например для ID оплаты для каждого товара)
		- One_To_Many - 



		method: 'POST',
  url: 'https://kopi34.ru/api/orders/check',
  headers: Headers {
    'x-vercel-ip-continent': 'NA',
    'x-vercel-ip-latitude': '39.0469',
    accept: '*/*',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    host: 'kopi34.ru',
    'x-vercel-ja4-digest': 't13d591000_a33745022dd6_1f22a2ca17c4',
    'x-vercel-proxy-signature-ts': '1734100420',
    'x-forwarded-for': '54.86.50.139',
    'postman-token': '58fdbb50-c481-4c00-910d-4f92558a89b7',
    'x-vercel-ip-country': 'US',
    'x-forwarded-proto': 'https',
    'x-vercel-ip-country-region': 'VA',
    'content-length': '7',
    'user-agent': 'PostmanRuntime/7.43.0',
    'x-real-ip': '54.86.50.139',
    'x-matched-path': '/api/orders/check',
    forwarded: 'for=54.86.50.139;host=kopi34.ru;proto=https;sig=0QmVhcmVyIDc2MWMwZmJmZjE2Yjg3YzRkNDY2ZDdlM2YyNzZiMzhhMzgxMTk3OTRkYmEwNzExMGQxNTc4OGE0Y2E3ODRlMWM=;exp=1734100420',
    'x-vercel-proxy-signature': 'Bearer 761c0fbff16b87c4d466d7e3f276b38a38119794dba07110d15788a4ca784e1c',
    'x-vercel-ip-as-number': '14618',
    'x-vercel-sc-headers': '{"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBsb3ltZW50SWQiOiJkcGxfN1VXbW84Qm9SYk11YWU0NHhZZ0poMkNldjRwTSIsInVubGltaXRlZCI6ZmFsc2UsInBsYW4iOiJob2JieSIsImRvbWFpbiI6ImtvcGkzNC5ydSIsImJsb2NrIjpmYWxzZSwiaWF0IjoxNzM0MTAwMTIwLCJwcm9qZWN0SWQiOiJwcmpfbzc1VEtHMTFyTlRmSE9BMjVzclJ6OHJxS3diSyIsImV4cCI6MTczNDEwMTA0MCwib3duZXJJZCI6InRlYW1fUEJHanMzWkdRVWNJZFc2NUl5eElCQ2dNIiwicmVxdWVzdElkIjoiNDVuZjItMTczNDEwMDEyMDA3NC04MzE4ODA0Y2JlMmYiLCJlbnYiOiJwcm9kdWN0aW9uIn0.NDE1RqSirBVlV5blNW6GnSofGrXppS2KY2kRKAQkGdQ"}',
    'x-vercel-proxied-for': '54.86.50.139',
    'x-vercel-ip-city': 'Ashburn',
    'x-vercel-internal-ingress-bucket': 'bucket0',
    'x-vercel-ip-longitude': '-77.4903',
    'x-vercel-deployment-url': 'kopi34-3-f8cj58ys4-jack-lees-projects-e61eae64.vercel.app',
    'x-vercel-ip-timezone': 'America/New_York',
    'x-vercel-sc-basepath': '',
    'x-vercel-sc-host': 'iad1.suspense-cache.vercel-infra.com',
    'x-vercel-id': 'iad1::45nf2-1734100120074-8318804cbe2f',
    'x-forwarded-host': 'kopi34.ru',
    'accept-encoding': 'gzip, deflate, br',
    'x-vercel-forwarded-for': '54.86.50.139',
    connection: 'close',
    'x-forwarded-port': '443'
  },
  destination: '',
  referrer: 'about:client',
  referrerPolicy: '',
  mode: 'cors',
  credentials: 'same-origin',
  cache: 'default',
  redirect: 'follow',
  integrity: '',
  keepalive: false,
  isReloadNavigation: false,
  isHistoryNavigation: false,
  signal: AbortSignal { aborted: false }
}