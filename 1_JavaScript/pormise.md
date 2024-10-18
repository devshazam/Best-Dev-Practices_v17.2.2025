```js
// https://learn.javascript.ru/promise-basics

firstAsynchronousFunction()
.then((res) => { // обязательная ф-ция - всегда исполняет внутреннюю ф-ции и передает туда результат промиса
  console.log(res.data);
})
.then((data) => {
    console.log(data);  // можно исполнять разные промисы 
    return promise2;
})
.then((data) => {
  console.log(data);  // Promise2 выполнен
  return promise2;
})
.catch((error) => { // выполнится в ответ на первую ошибку в цепочке промисов
  console.log(error.name + error.message);
})
.finally(() => { // выполниться в не зависимости от резуольтата 
  console.log(`All Tasks is Done`); 
})





async () => {
  try {
    const res = await firstAsynchronousFunction();

    console.log(res.data);
  } catch(error) {
    console.log(error.name + error.message);
  } finally {
    console.log(`All Tasks are Done`);
  }
}
  // Использование циклов  - https://sliceofdev.com/posts/promises-with-loops-and-array-methods-in-javascript



// =========================================================================>

https://sliceofdev.com/posts/promises-with-loops-and-array-methods-in-javascript

циклы для промисов

- for of (для массивов) - этот цикл последовательно выполняет каждый промис по завершению предыдущего

- map - 





// ==========================================================================>

Event Loop:
  http://latentflip.com/loupe/?code=Y29uc29sZS5sb2coJ0ZpcnN0IDAnKTsKY29uc29sZS5sb2coJ0ZpcnN0IDEnKTsKCmZ1bmN0aW9uIGZuMSgpIHsKICAgY29uc29sZS5sb2coJ0ZpcnN0IDInKTsKfQogc2V0VGltZW91dChmbjEsIDMwMDApOwo%3D!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D
  https://medium.com/@lydiahallie/javascript-visualized-promises-async-await-a3f1aad8a943
  Event Loop - это процесс управляющий исполнением кода в js
    - Синхронные задачи
      - весь код запускается в call stack
        - синхронные ф-ции исполняются сразу
        - асинхронные ф-ции отправляются на исполнение в WEB API 
      - WEB API после завершения асинхронных ф-ций отправляет 