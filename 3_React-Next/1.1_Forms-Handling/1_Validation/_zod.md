# 1
	> Пример - https://dev.to/banerjeeprodipta/validate-file-with-zod-20o
	const contactFormSchema = z.object({
	apiKey: z.string().trim().min(1, { message: "Name field is required" }),
	email: z.string().email({ message: "Invalid email address" }),
	apiSecret: z.string().trim().min(1, { message: "Please type in a message" }),
});
		- trim() - подрезать проеблы по краям строки