1_CDN
    CDN (сеть распределения контента)





- lazy-load vs suspence - https://sitedominion.medium.com/lazy-vs-dynamic-loading-components-in-next-js-7c4b1775f9b0
- "use client" - ,tp кешированияя и предрендеринга - использовать по минимуму
- Ссылки
    - <Link href="/dashboard" prefetch={false}> - в зоне экрана все ссылки предварительн скачиваются - для предотвращения prefetch
    - rel="nofollow"


- PostCss
    - autoprefixer 

##  next.config.js
    - Ref: https://medium.com/@halilatilla/removing-console-logs-in-next-js-projects-c55713a9f635
        module.exports = {
            compiler: {
                    // Remove all console logs
                removeConsole: true 
                    // Remove all console logs, excluding error logs
                removeConsole: { exclude: ["error"] }
                    // Remove console logs only in production
                removeConsole: process.env.NODE_ENV === "production"
                    // Remove console logs only in production, excluding error logs
                removeConsole: process.env.NODE_ENV === "production" ? { exclude: ["error"] } : false
            }
        };