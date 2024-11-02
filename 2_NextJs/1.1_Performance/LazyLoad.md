3_Верхняя часть страницы в приоритете оптимизации - LSP
4_Паралельная выборка данных - https://nextjs.org/learn/dashboard-app/fetching-data
    - При последовательной загрузке загрузка данных превращается в водопад (следуещее начинается только после заревшения предведущего), но можно вызвать паралельно:
        const data = await Promise.all([
        invoiceCountPromise,
        customerCountPromise,
        invoiceStatusPromise,
        ]);

5_Static and Dynamic rendering  
    - Nextjs по молчанию делаем статический рендеринг с кешированием маршрутов
    - НО, если код маршрута содержит ф-ции запросов - то nextjs выполняет динамический рендеринг
- Streaming vs Dynamic
    - https://nextjs.org/docs/app/building-your-application/optimizing/lazy-loading
6_ SSG - это генерация статического контента

2_import Script from 'next/script';
    <Script src="https://example.com/third-party.js" strategy="lazyOnload" />



const ClientComponent = dynamic(() => import('./ClientComponent'), {
  loading: () => <p>Loading...</p>,
});
