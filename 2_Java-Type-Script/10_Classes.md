# Классы - https://learn.javascript.ru/class
		class MyClass {
			constructor(firstName = "John",lastName= "Doe",age = 0,gender = "Male"){
				this.firstName = firstName
				this.lastName = lastName
				this.age = age
				this.gender = gender

				<!-- Альтернативный вариант -->
				Object.assign(this, { firstName, lastName, age, gender });

			}

			method(...) {} // метод
			get something(...) {} // геттер
			set something(...) {} // сеттер

			static staticMethod(word){
				return "Welcome to Planet Earth " + word
			}
		}