# Server Action
	- Новая тенденция не возвращать ничего в ответ на запрос к Server Action, а вызывать ф-ции ревалидации и перенаправления
		-   if (!user) redirect("/"); или   if (!user) return redirect("/");
			- import { redirect } from "next/navigation";
			- import { revalidatePath } from "next/cache";