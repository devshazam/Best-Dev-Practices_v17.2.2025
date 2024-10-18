# Зачем нужны менеджеры состояния
    - для обработки аутентификации на сайте
    - для обработки карзины насайте
        - Zustand - вместе с методом persist





```js


import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";

const schema = z.object({
  email: z.string().email({
    message: "Please enter a valid email",
  }),
  password: z.string().min(8, {
    message: "Password must be at least 8 characters",
  }),
});

type FormSchema = z.infer<typeof schema>;

export default function App() {
  const { register, handleSubmit, formState: { errors }, } = useForm < FormSchema >
  {
    resolver: zodResolver(schema),
    defaultValues: {
      email: "",
      password: "",
    },
  };

  const onSubmit = (data: FormSchema) => {
    console.log(data);
  };

  return (
    <main className="h-screen grid place-items-center">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="w-full max-w-xl bg-white shadow-lg border p-8 rounded-lg"
      >
        <div className="mb-4">
          <label htmlFor="email" className="block mb-2">
            Email adress
          </label>
          <input
            id="email"
            type="email"
            {...register("email")}
            placeholder="Email address"
            className="w-full outline-none p-3 border focus:border-2 focus:border-blue-600 rounded-lg"
          />
          {errors.email && (
            <p className="text-sm text-red-600 mt-1">{errors.email.message}</p>
          )}
        </div>

        <div className="mb-4">
          <label htmlFor="password" className="block mb-2">
            Password
          </label>
          <input
            id="password"
            type="password"
            {...register("password")}
            placeholder="Password"
            className="w-full outline-none p-3 border focus:border-2 focus:border-blue-600 rounded-lg"
          />
          {errors.password && (
            <p className="text-sm text-red-600 mt-1">
              {errors.password.message}
            </p>
          )}
        </div>
        <button
          className="w-full rounded-lg p-3 bg-blue-600 text-white"
          type="submit"
        >
          Login
        </button>
      </form>
    </main>
  );
}