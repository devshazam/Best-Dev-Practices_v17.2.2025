/** @type {import('next').NextConfig} */
const nextConfig = {
    // experimental: {
    // },
		removeConsole: true, // Отключить вывод консоли
        sassOptions: { // подгружает переменные во все модули scss
            prependData: `@import 'app/variables';`,
        },
};

export default nextConfig;
