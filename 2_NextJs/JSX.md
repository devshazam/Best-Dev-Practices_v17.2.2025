
```js
- let m1 = <p> test </p>;
- {arr} // выводит весь массив последдовательно 

- IF
    - {show ? <p>text1</p> : <p>text2</p>} // вернет первый обзац если переменная show == true и тд.
    - {show && <p>text</p>} // если true то выведет или ничего не вернет в обратном случае

- Function
    onClick={showMess} // () => {return 2;}
    onClick={() => showMess('user')} // (var) => {return var;}
    onChange={(e) => setDescriptionText(e.target.value)}
    onClick={event => func('eee', event)} // 

- arr.map((item, index) => {
        return (
            <p key={index}>{item}</p>;
        );
    }) 
```

