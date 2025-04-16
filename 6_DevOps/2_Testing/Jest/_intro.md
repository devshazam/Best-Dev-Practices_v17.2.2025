1. Тестирование
    - Ref: 
        - https://nextjs.org/docs/app/building-your-application/testing/jest
        - https://medium.com/@shuvo_tdr/testing-next-js-applications-with-jest-a-comprehensive-guide-48cffa37110b
    1_ `__tests__` - папка для тестирования
    2_ `npm init jest@latest` - создание конфигурационного файла в root
        - `./templates/jest.config.ts`
    3_ `packege,json` - внести 
          "scripts": {
                "test": "jest",
                "test:watch": "jest --watch"
            },
    4_ 
2. Unit тестирование - это тестирование отдельных модулей в основном ф-ций