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

