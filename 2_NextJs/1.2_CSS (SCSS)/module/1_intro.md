# 

- в модуле видны переменные из глобального файла css (scss)
- Создание модуля css для отдельного компонента производится добавлением его имени к модулю:
    - [имя].module.css (.scss)
- Именование слассов в модулях:
    - kebab-case
        - При именовании в этом стиле доступ к классам осуществляется с попощью 
        - className={styles['class-name']}
    - camelCase
        - При именовании в этом стиле доступ к классам осуществляется с попощью 
        - className={styles.className}
- global
    - создает глобальный класс, который будет виден во всех компонентах
        :global .text-center {
            text-align: center;
        }
- composes
    - наследование классов 
        .classOne{
            color: red;
        }
        .classTwo{
            composes: classOne;
            width: 100%;
        }