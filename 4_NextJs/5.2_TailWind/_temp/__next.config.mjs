/** @type {import('next').NextConfig} */
const nextConfig = {
    // experimental: {
    // },
        sassOptions: {
            prependData: `@import 'app/variables';`, // подгружает переменные во все модули scss
        },
};

export default nextConfig;