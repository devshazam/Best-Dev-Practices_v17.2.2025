HTTP(s) - Hypertext Transfer Protocol (secure) - «протокол передачи гипертекста»
    SSL - certyficat
    TLS -  transport layer security — Протокол защиты транспортного уровня[1])

starting line
    starting line (request)
        GET /page/test HTTP/1.1
            GET
            POST
    starting line (response)
        HTTP/1.1 200 OK
            200 - success
            3xx - redirection
            4xx - client error
            5xx - server error

Headers
    Headers  (General Headers)
        Host: example.com // название хоста
        Date: Wed, 21 Oct 2020 07:28:00 GMT // время запроса
        Last-Modified: Sat, 16 Jan 2020 21:16:42 GMT // время последнего изменения контента
        Content-Type: text/html; charset=utf-8 // тип передаваемых данных
            Content-Type: text/html
            Content-Type: text/css
            Content-Type: application/json
        Content-Language: ru
        Content-Length: 10000
    Headers (custom)
        X-Powered-By: "Express" // 

BODY
    html
    json
