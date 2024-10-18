# 1 Naming Convention:
    -


Comments:
    # <- Это знак коментариев

ENV:
    pip3 install virtualenv
        <!-- windows -->
            python -m venv venv
            .\venv\Scripts\activate
            .\.venv\Scripts\activate
        <!-- Linux -->
            virtualenv --python=python3 venv
            source venv/bin/activate

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt

IMPORT:
    import example # так импортируют модуль с именем example.py
        example.do_jump() # так обращаются к функциям и переменным импортируемого класса
    import example as mx # Алиас - переименование при импортировании модуля с именем example.py
        mx.ple.do_jump() # так обращаются к функциям и переменным импортируемого класса
    from example import do_jump # Импортирование только нужных переменных с модуля с именем example.py
        do_jump()

NAMING:
    Modules -> math_operations.py
    Variables and Functions:
        -> local_variable = 5 # Локальный переменные в рамках функций
        -> GLOBAL_VARIABLE = 10 # Глобальные переменные
    СЩТSTANTS -> PYTHON_CONSTANT

ERRORS:
    

COMMON:

    len()

    var[0]

    txt = 'abcde'
    res = txt[1:3:1] # [start:stop:step]
    print(res) # выведет 'bc'

    res = 1 in lst

    https://www.pythonmorsels.com/assignment-versus-mutation/
    Строки и числа неизменяемы
    Списки и словари изменяемы