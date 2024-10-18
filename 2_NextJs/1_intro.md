# 1 Naming Convention: - https://dev.to/sathishskdev/part-1-naming-conventions-the-foundation-of-clean-code-51ng
  - Variable Names
      const userName = "sathishskdev";
  - Function Names
      const getFullName = () => {...}
  - Constants
      const BASE_PATH = "https://domain.services/api";
  - Object Properties
      const user = { userName: "sathishskdev" }

  - React Component
      const Todo = () => {...} // PascalCase
  - root
    ├ app // folder names kebab-case
    │ ├ not-found.tsx // kebab-case
    │ ├ page.tsx // kebab-case
    └ components // folder names kebab-case
      ├ Button.tsx // PascalCase
      └ Button.modules.css // PascalCase

  - Css file mames
      Todo.module.scss // PascalCase
  - Css classes in global css
      .header-container { display: "flex"; } // kebab-case
  - Css classes in module css
      .headerContainer { display: "flex"; }


# Категоризация папок 
    0 - Ошибки и производительность
    1 - Базовые знания верстки
    2 - Специальный знания NextJs
    5 - Сторонние библиотеки



2_ Параметр роитинга [id]
        export default async function Page({ params }: { params: { id: string } }) {
                const id = params.id;
                // ...
        }




-   Jquery можно использовать через npm
    -   https://www.npmjs.com/package/jquery
        - ЭТО РАБОТАЕТ ТОЛЬКО в браузере - "use client"
        - после этого можно испольховать любой код jquery



- Поисковые параметры
  - useSearchParam - работают только на клиенте!!
  - На сервекре:
    - export async function GET(req: any, res: any){
    console.log( req.nextUrl.searchParams.get('search-key')


- ENV - все переменные по умолчанию сервенные, чтобы сделать их доступными в клиенте нужно добавить NEXT_PUBLIC_
    - console.log(process.env.NEXT_PUBLIC_REACT_APP_YANDEX_KEY )




