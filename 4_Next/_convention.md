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

## Error: console.log() в серверных аомпонентах не видны в консоли браузера
    - ref =
    - key = console.log()
    - desc = console.log() в клиентских компонентах выводится в консоль браузера, а в серверных в терминал!
    - sol = console.log() в клиентских компонентах выводится в консоль браузера, а в серверных в терминал!

## 'useClient'
	- Дочерние елементы клиентского компонента АВТОматически становятся клиентскими

## environment variabels
	- Для использования переменной из .env файла в клиентских компонентах - ее нужно сделать публичной, добавив вначале `NEXT_PUBLIC_`
