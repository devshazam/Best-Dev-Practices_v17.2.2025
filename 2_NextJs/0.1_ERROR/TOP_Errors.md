=== 
    - Error: Objects are not valid as a React child (found: object with keys {children}). If you meant to render a collection of children, use an array instead.
    - Причина: попытка отобразить в компоненте пропс-объект (`{props}`) вместо отображения елементов пропса(`{props}`)
  
===
    - Error: Hydration failed because the initial UI does not match what was rendered on the server.
    - Причина: расширение браузера меняющие цвета сайта

===
- В цикле map нельзя заворачивать элемент ы пустые кавычки, а нужно верхний элемент задавать key props
     {globalParamsObject.discounts.discountsCategory.map(
                                    (item: string, index: number) => {
                                        return (
                                            <Select.Option key={index + 1} value={index + 1}>{item}</Select.Option>
                                        );
                                    }
                                )}