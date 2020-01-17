// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@/api/axios'
import api from './api/api'
import store from './store'
import echarts from 'echarts'
import kityminder from 'vue-kityminder-editor'
// 全量引入 bk-magic-vue
import bkMagic from 'bk-magic-vue'
// 全量引入 bk-magic-vue 样式
import 'bk-magic-vue/dist/bk-magic-vue.min.css'


Vue.config.productionTip = false;
Vue.use(kityminder)
Vue.use(ElementUI);
Vue.use(bkMagic)
Vue.use(Vuex);
// 引入echarts
Vue.prototype.$echarts = echarts
// 将API方法绑定到全局
Vue.prototype.$api = api;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
