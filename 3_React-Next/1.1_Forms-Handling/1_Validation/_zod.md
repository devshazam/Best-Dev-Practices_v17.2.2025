# 1
	> Примерs
		https://dev.to/banerjeeprodipta/validate-file-with-zod-20o
		https://dev.to/strapi/form-validation-in-typescipt-projects-using-zod-and-react-hook-form-49g6
		https://github.com/MarcosMaio/Beautiful-Form-Register/blob/main/src/app/register-user/components/Register.tsx

		
	const contactFormSchema = z.object({
	apiKey: z.string().trim().min(1, { message: "Name field is required" }),
	email: z.string().email({ message: "Invalid email address" }),
	apiSecret: z.string().trim().min(1, { message: "Please type in a message" }),
});
		- trim() - подрезать проеблы по краям строки