# https://learn.javascript.ru/url
1. 
2. Добавить поисковые параметры 
	var url = new URL("http://foo.bar/?x=1&y=2");

	// If your expected result is "http://foo.bar/?x=1&y=2&x=42"
	url.searchParams.append('x', 42);

	// If your expected result is "http://foo.bar/?x=42&y=2"
	url.searchParams.set('x', 42);
2. Объект содержит следующие параметры:
	URL {
		href: 'https://javascript.info/profile/tester',
		origin: 'https://javascript.info',
		protocol: 'https:',
		username: '',
		password: '',
		host: 'javascript.info',
		hostname: 'javascript.info',
		port: '',
		pathname: '/profile/tester',
		search: '',
		searchParams: URLSearchParams {},
		hash: ''
	}