- Концепции языка TypeScript
    - Тип переменным задается явно (самостоятельно) и автоматически при объявлении
    - Тип нужно объявлять для переменных , ф-ций, цикла for


- строки, числа и boolean не изменяемы, а массивы и объекты изменяемы
    - 
- 
- as - переопределяет тип любой переменной
    -   let x2:string = morseCode.split('   ').map((x:string) => {
            console.log(x.split(' '))
            let x3 = x.split(' ')
            return x3.map((z2:any) => x1[z2 as keyof typeof x1]).join('')
            }).join(' ')
        console.log(x2)
        return x2