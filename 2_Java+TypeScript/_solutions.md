## нахождение промежутка
        -const X_2 = [[0, 1], [1, 5], [5, 10], [10, 50], [50, 100], [100, 500], [500, Infinity]].findIndex((elem) => X_1 >= elem[0] && X_1 < elem[1])

## конвертироватьстроковый символ в бинарную строку
        - var a = 'a'.charCodeAt(0).toString(2); 

## удалить все дубли из массива
        - uniqueArray = a.filter(function(item, pos) { return a.indexOf(item) == pos; })

## Поменять значения переменных местами если одно больше другого
        if(x2.length > x1.length) [x1, x2] = [x2, x1];