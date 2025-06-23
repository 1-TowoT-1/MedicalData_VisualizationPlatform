module.exports = {
    devServer: {
        proxy: {
            // 指定所有以 /api 开头的请求（例如 /api/getHomedata）都要代理到 Flask 后端。
            '/api': {
                // 要代理到的目标服务器
                target: 'http://localhost:5000', 
                changeOrigin: true,
                pathRewrite: {
                    // 例如，将 /api/getHomedata 重写为 /getHomedata，这保证后端的 Flask 实际收到的路径是正确的。
                    '^/api': '',
                },
            },
        },
    },
};