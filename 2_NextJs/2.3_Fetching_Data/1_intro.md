# Варианты получения информации с попощью запросов

## Server Component
    - toAPI Асинхронный запрос из асинхронной ф-ции
    - toDB
### API
    - размещение логики запросов и обработки информации в разделе '@/app/api/...' в файлах route.ts

## Client Component
    - React Query (recommended)
    - SWR
        - toAPI Асинхронная декларация и вызов из useEffect

## Server Action (experimental)
    - 'use server'
        - может вызываться из как из тега <form action{}>, так и любым другим обращзом