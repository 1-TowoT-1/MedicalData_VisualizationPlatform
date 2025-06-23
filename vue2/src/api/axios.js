import axios from "axios";

const axiosInstance = axios.create({
    baseURL: '/api',
    timeout: 5000
})

// 配置拦截器
axiosInstance.interceptors.request.use(
    (config) => {
        return config;
    },
    (error) => {
        return Promise.reject(error);
    },
)

axiosInstance.interceptors.response.use(
    (response) => {
        return response.data
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default axiosInstance;