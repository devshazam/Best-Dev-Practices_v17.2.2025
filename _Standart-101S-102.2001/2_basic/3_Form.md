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

# formData
        // if(file)formData.append('files', file);
        // if(fileList[0] && fileList[0].thumbUrl) {const B64_TO_BLOB = b64toBlob(fileList[0].thumbUrl.split(",")[1], 'image/jpg');
        // if(fileList[0] && fileList[0].thumbUrl) formData.append('files', fileList[0].thumbUrl);
        // if(file)formData.append('files1', B64_TO_BLOB);}