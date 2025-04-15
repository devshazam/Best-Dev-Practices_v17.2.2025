1. Передача пропсов (Props)
	- <PdfComponent {...{date: e.createdAt, feature: e.feature, description: e.description, office: e.office}} />
		- function PdfComponent({date, feature, description, office}: any){...}
		- https://stackoverflow.com/questions/49081549/passing-object-as-props-to-jsx
2. Основны работы с REACT
	- useState - может работать с массивами и объектами
	- useEffect - если в качестве зависимости использовать объект или массив - то произойдет ошибка = стейт будет бесконечно перерендериваться!
		- sol JSON.stringify(orderList)