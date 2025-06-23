import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import dataV from '@jiaminghi/data-view'
import VueParticles from 'vue-particles'

import "swiper/swiper.min.css"
import * as echarts from 'echarts';
import "@/utils/echarts-wordcloud.min.js"
import axios from '@/api/axios'

Vue.use(VueParticles)
Vue.use(dataV)
Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.prototype.$echarts = echarts

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')