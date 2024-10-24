## Принцыпы обработки полей
    - Контролируемые 
        - Без тега <form>
        - у каждого input есть свой value и onChange, которые хранятся и передаются через useState
    - Не контролируемые
        - С тегом <form>
        - у каждого input есть атрибут name, но нет value и onChange
        - Информация обрабатывается и передается при помощи 
            `const formData = new FormData(event.target)`