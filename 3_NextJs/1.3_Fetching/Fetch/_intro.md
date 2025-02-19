#	
	- Sevrer
```js
		const data = await fetch('https://api.vercel.app/blog')
  		const posts = await data.json()
```
	- Client
```js
			useEffect(() => {
				async function fetchPosts() {
				const res = await fetch('https://api.vercel.app/blog')
				const data = await res.json()
				setPosts(data)
				}
				fetchPosts()
			}, [])	
```