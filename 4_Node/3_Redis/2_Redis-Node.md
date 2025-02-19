# Install
	$ npm install redis

# Usage
```js
	const redis = require('redis')

	const client = redis.createClient({
		url: 'redis://localhost:6379',
	})

	client.on('error', function (error) {
	console.error(error)
	})

	  	client.get(key, (error, reply) => {
			if (error) res.send('Error')
			else res.send(reply)
		})

		client.set(key, data, (error, reply) => {
			if (error) res.send('Error')
			else res.send(reply)
		})

```