## Использование useState в качестве зависимости useEffect - https://profy.dev/article/react-useeffect-with-object-dependency
    1_ 
        useEffect(() => {
            ...
        }, [JSON.stringify(filters)]);
    2_
        useEffect(() => {
            ...
        }, [...Object.values(filters)]);