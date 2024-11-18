# Server Action
	- intro: 
		- Вызов черезх <form action={...}>
			- Сервер акшены созданы для передачи formData в POST запросе с клиента на сервер
				- Передача дополнительных аргументов возможна при помощи метода bind (https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/#instrument-nextjs-server-actions)
		- Вызов через события (https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations#event-handlers)
			- аргументы можно добавлять произвольно