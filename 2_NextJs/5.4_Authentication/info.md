- http://localhost:3000/api/auth/callback/credentials
    - по умолчанию 
            - /api/auth/callback/credentials - ответ с данными от формы
            - /api/auth/signin - автоматическая форма

```js
export const authConfig // объект с параметрами работы аутентификации
  debug: true, // дополнительная информация об ошибках (только для режима разработки)
  providers: [] // массив с провайдерами
  callbacks: {

        Credentials // провайдер работающий с формой входа на сайте
                credentials: // https://next-auth.js.org/providers/credentials
                        {username: { label: "User Name",} }, // параметры для автоСгенерированной формы входа на сайт
                        {password: { label: "Password", type: "password" } },
                authorize(c): <User | null> {...} // функция проверки пароля
