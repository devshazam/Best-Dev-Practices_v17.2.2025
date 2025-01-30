# _convention_ 
    - React Component
      const ToDo = () => {...} // PascalCase
    - root
	   ├ actions
        ├ app // folder names kebab-case
        │ ├ not-found.tsx // kebab-case
        │ ├ page.tsx // kebab-case
        ├ components // folder names kebab-case
	   │ ├ ui
	   │ ├ layout
	   │ ├ templates
	   │ └ pages
	   │ 	├ Button.tsx // PascalCase
	   │		└ Button.modules.css // PascalCase
	   ├ config
	   ├ lib
	   │	├ hooks
	   │ ├ types
	   │ ├ utils
	   │ └ providers
	   └ store // для хранения состояний (zustand, redux, mobx)


    - CSS
        - Todo.module.scss // PascalCase
        - .header-container { display: "flex"; } // kebab-case
        - .headerContainer { display: "flex"; } // Css classes in module css
