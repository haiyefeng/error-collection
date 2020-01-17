import { $axios } from './axios'
export default {
// 获取错题集
    getMistake: function () {
        return $axios.get('/misset/mistakes/')
    },
    // 创建错题集
    createMistakes: function (params) {
        return $axios.post(`/misset/mistakes/batch_create/`, params)
    },
    // 查看总结
    getSummary: function (params) {
        return $axios.get('/misset/summary/get_mptt_summary/', params)
    }
}