import Vue from 'vue'
import axios from 'axios'

axios.defaults.baseURL = window.siteUrl;
axios.defaults.withCredentials = true;

axios.interceptors.request.use(config => {
    config.headers['X-Requested-With'] = 'XMLHttpRequest';
    let regex = /csrftoken=([^;.]*).*$/;
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
    return config
});

axios.interceptors.response.use(response => {
    if (response.status >= 400) {
        return {
            code: response.status,
            message: '请求异常，请刷新重试',
            result: false
        }
    }
    return response.data
}, error => {
    if (error.response.status) {
        return {
            code: 403,
            message: error.response.data.message,
            error: error,
            result: false
        }
    }
    return {
        code: 500,
        message: '未知错误，请刷新重试',
        error: error,
        result: false
    }
});
Vue.prototype.$axios = axios;
export const $axios = axios;
