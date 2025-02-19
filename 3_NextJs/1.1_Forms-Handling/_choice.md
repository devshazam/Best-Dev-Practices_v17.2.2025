# Лучшие подходы при работе с формами
	- useActionState + ServerActions + zod
		- ⚠️ использовать: useActionState (useFormState устарела)
	- ⚠️ React-Hook-Form - для каждой библиотеки UI требуется свой хук:
		- react-hook-form-antd - для AntD 


# Не лучшие подходы при работе с формами
    - Uncontrolled с <form> без value и onChange на input-ах
        - Информация обрабатывается и передается при помощи 
            `const formData = new FormData(event.target)`
    - Controlled без <form>, но с value и onChange на input-ах
        - const [formData, setFormData] = useState({ name: '', email: '' });
        - <input value={formData.name} />
        - const handleChange = (e) => { setFormData({ ...formData, [e.target.name]: e.target.value }); }
        - Без тега <form>
        - у каждого input есть свой value и onChange, которые хранятся и передаются через useState
