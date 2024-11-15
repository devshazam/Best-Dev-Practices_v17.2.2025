# 1 Naming Convention: 
    - React Component
      const ToDo = () => {...} // PascalCase
    - root
        ├ app // folder names kebab-case
        │ ├ not-found.tsx // kebab-case
        │ ├ page.tsx // kebab-case
        └ components // folder names kebab-case
        ├ Button.tsx // PascalCase
        └ Button.modules.css // PascalCase
    - CSS
        - Todo.module.scss // PascalCase
        - .header-container { display: "flex"; } // kebab-case
        - .headerContainer { display: "flex"; } // Css classes in module css

## Error: reading property of undefined
    - ref = 
    - key = <Link> 
    - desc = При переходе между страницами сайта с использованием <Link> стейты в zustand не обновляются!
    - sol = замена <Link> на <a>

## 'useClient'
	- Дочерние елементы клиентского компонента АВТОматически становятся клиентскими

## environment variabels
	- Для использования переменной из .env файла в клиентских компонентах - ее нужно сделать публичной, добавив вначале `NEXT_PUBLIC_`
