#
	.flex-container{
		display: flex;

		justify-content: 	// выравнивание между flex элементами горизинтальное
							center		// по центру
							flex-start  	// с лева
							flex-end		// с права
							space-around 	// пространства около
							space-between	// пространство между
							space-evenly	// одинаковые отступы со всех сторон

		align-items:		// Вертикальное выравникавание
							center		// по центру
							flex-start	// по верху
							flex-end		// с низу
							stretch		// растянутся
							baseline		// по центральной линии
							normal		// 

		flex-flow: // короткое св-во для flex-direction flex-wrap

			flex-direction: 	// направление 
							row			// default строка
							column		// столбец
							row-reverse	// строка в обратную сторону
							column-reverse	// столбец в обратную сторону
			
			flex-wrap:			// перенос 
							nowrap		// default не переносить
							wrap			// переносить на следующую строку или столбец
							wrap-reverse	// переносить в обратнном порядке

		
	}