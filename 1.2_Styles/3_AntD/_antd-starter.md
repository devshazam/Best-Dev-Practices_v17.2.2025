# 
```js
# Grids:
	<Row gutter={[16, 16]} justify={'start'} align={'top'}>
		<Col xs={24} md={8}>
		</Col>
	</Row>

- Skeleton:
	 <Skeleton active paragraph={{ rows: 8 }} avatar/>
	 // active - анимация волны
	 // avatar - добавление кружочка в начале 
	 // paragraph - кол-во строк

- Input Group:
	<Col md={12} xs={24}>
		<InputNumber
			min={1}
			max={100000}
			placeholder="Масса"
			className="w-full "
			onChange={(value: number | null) => {
				if (!value) { changeCardData( item["name"], 0) }else{
					changeCardData( item["name"], value)
				}
			}}
		/>
	</Col>

- Grid
	<Row>
		<Col span={24}>
			<Col md={12} xs={24}>