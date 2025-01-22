# 1 Naming Convention:



background:
    background: #ffffff url("img_tree.png") no-repeat right top; // картинка
    background-image: linear-gradient(red, yellow); // Градиент

Display:
    Inline - <a>, <span>, <img> // занимает только размер контента width и height НЕ работают, не прервывает строку
    Inline-block - // занимает только размер контента width и height можно задавать, не прервывает строку
    block - <p>, <div>, <h1> // занимает всю доступную ширину, прерывает строку

Align: https://www.w3schools.com/css/css_align.asp
    <div>
        margin: auto
    text
        align-text: center
        line-height: 50px
    common
        Flexbox


transition: width 2s, height 4s; // плавное изменение от одного класса в другой

Pseudo
    Classes
        :hover
    Element
        ::after
        ::befor

Width:
    ABS
        px
    REL
        vw - 1% от ширины экрана
        hw - 1% от высоты экрана
        %
        em - относительно размера шрифта 
        rem - относительно размера корневого элемента
    Calc
        calc(100% - 100px);

Sprites
    #home {
        width: 46px;
        height: 44px;
        background: url(img_navsprites.gif) 0 0;
        }

Margin
    - ! margin только между братьями (елементами), для растояния между родителем и потомком - padding
    - Margin Collapse   
        - использовать только нижний margin
        - 
Padding
    - ! нужен для растояния между родителем и потомками
    - 