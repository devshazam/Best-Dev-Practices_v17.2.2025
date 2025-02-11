# Основы:
	- margin - отступы между одинаковыми элементами одного родителя
	- padding - отступы между границей и всеми детьми элемента
	- 
# Блоки: 
	> Выравнивание - https://www.w3schools.com/Css/css_align.asp
		> Горизонтальное выравнивание:
			- block: margin-x: auto;
			- text: 
				- align-text: center
				- line-height: 50px
		> Вертикальное выравнивание:
			- Flexbox
	> Ширина
		- является зависимой от ширины экрана
		- max-width: 1200px; - определяет максимальную ширину 
	> Высота
		- расширяемая контентом и отступами
			- При необходимости больших отступов нужно использовать FlexBox
			- min-height: 350px; - определяем минимальный отступ
	> Display
		- Inline - <a>, <span>, <img> // занимает только размер контента width и height НЕ работают, не прервывает строку
		- Inline-block - // занимает только размер контента width и height можно задавать, не прервывает строку
		- block - <p>, <div>, <h1> // занимает всю доступную ширину, прерывает строку
# Основные Свойства
	> Text
		- text-align:
			- justify - выравнивание по всей ширине
		- text-decoration: underline red double 5px; (line, color, style, thikness) - общее свойство для стилизации зачеркивания
		- text-transform: uppercase | lowercase;
		- text-indent: 50px; - отступ красной строки
		- letter-spacing: 5px; - расстояние между буквами
		- line-height: 0.8; - высота строки
		- word-spacing: 10px; - расстояние между буквами
		- white-space: nowrap; - перенос строки
	> Background
		- background: #ffffff url("img_tree.png") no-repeat right top; - установка картинки в качестве фона
		- Sprites: #home { width: 46px; height: 44px; background: url(img_navsprites.gif) 0 0; }
	> Border
		- border: 5px solid red; - граница блока
	> List
		+ list-style: square inside url("sqpurple.gif");
			- list-style-type: circle; - стиль отображения маркеров списка
				- list-style-image: url('sqpurple.gif'); - отображение маркеров картинкой
			- list-style-position: outside / inside; - маркеры отображаются за пределами элемента или в перделах
	> Pseudo
		- Classes
			:hover
		- Element
			::after
			::befor
	> Width:
		- ABS
			px
		- REL
			vw - 1% от ширины экрана
			hw - 1% от высоты экрана
			%
			em - относительно размера шрифта 
			rem - относительно размера корневого элемента
		- Calc
			calc(100% - 100px);
			width: max(50%, 300px);
	