- 'next.congig.mjs
    - output: 'export', // это позволит собрать приложение как статическое
    - images: {  // это позволит не оптимизировать картинки, потому что им нужен для этого сервис, а без него они не будут выводится
    unoptimized: true,
  },
    
- generateStaticParams() // добавить эту ф-цию к динамическим роуам что-бы сгенерировать страницы - без него будет ошибка
    - https://www.geeksforgeeks.org/next-js-functions-generatestaticparams/
     
- npm run build
- 'out' // копируем все на хостинг из папки 