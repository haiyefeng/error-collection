const state = {
  isCollapse: true // 左侧菜单是否收缩
}

const getters = {
  isCollapse: state => state.isCollapse
}

const mutations = {
  setIsCollapse (state, isCollapse) {
    state.isCollapse = isCollapse
  },
}

const actions = {}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
