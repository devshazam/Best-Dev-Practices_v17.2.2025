# GET
    - В запросе get может передоваться:
        - url
        - Search params ?param1=1&param1=1
    
# POST
    - В запросе post может передоваться в теле запроса:
        - JSON | string
            - base64 (строка) - передача картинки
        - formData
            - Blob (без кодирования, форма сделает это сама)
        - Blob/BufferSource
        - URLSearchParams для отправки данных в кодировке x-www-form-urlencoded

# Input 
    - input file - предоставляет url = "blob:http://example.com/12345"
        - Преобразование в BLOB - означает что  картинка скачается
        - 