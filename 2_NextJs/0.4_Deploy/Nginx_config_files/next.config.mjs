/** @type {import('next').NextConfig} */
const nextConfig = {

    // СТАТИЧЕСКАЯ ГЕНЕРАЦИЯ САЙТА
    output: 'export',
    trailingSlash: true,
    skipTrailingSlashRedirect: true,
    distDir: 'dist',
    images: {
        unoptimized: true,
    },
    // 

};

export default nextConfig;
