# winston - node logging
	1_ Add logger.js file to root dir
```js
	// logger.js - at root dir
	import winston from "winston";
	const { combine, timestamp, json } = winston.format;

	const logger = winston.createLogger({
	level: "info",
	format: combine(timestamp(), json()),
	transports: [
	new winston.transports.File({ 
		filename: "app.log"
	}),
	],
	});

	export { logger };
```
	2_ Add app.log file to root dir
	3_ Use logger only within server-component
```js
  	import { logger } from "@/logger"; // our logger import

	logger.info(`вызов из серверАктиона - Testing`);
```