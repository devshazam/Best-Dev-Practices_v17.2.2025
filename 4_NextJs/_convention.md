# 1 Naming Convention: 
(https://dev.to/sathishskdev/part-1-naming-conventions-the-foundation-of-clean-code-51ng)
    - JavaScript:
        - let userName = "sathishskdev";
        - const getFullName = () => {...}
        - const BASE_PATH = "https://domain.services/api";
        - const userNames = { userName: "sathishskdev" }

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

