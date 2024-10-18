https://www.freecodecamp.org/news/write-html-css-faster-with-emmet-cheat-codes/

lorem
    30 words
lorem10
    10 words

.test
    <div class="test"></div> 
#test
    <div id="test"></div> 
.test*2
    <div class="test"></div> 
    <div class="test"></div> 
.test+.test2
    <div class="test"></div> 
    <div class="test2"></div> 
.test>.test2
    <div class="test">
        <div class="test2"></div> 
    </div>     
.test>(header>a)+footer>p
    <div class="test">
        <header>
            <a href=""></a>
        </header>
        <footer>
            <p></p>
        </footer>
    </div>     




###### Не используется из-за переусложненности
'^' - перейти вверх вложенности
'{..}' - вложенный текст в тег
    p{This is a paragraph} —> <p>This is a paragraph</p>
'*' - колл-во элементов 
    '$' - переменная счета элементов
