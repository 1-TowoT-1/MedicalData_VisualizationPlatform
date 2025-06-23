<template>
  <div class="tableData-container">
      <transition name="fade" mode="out-in">
        <dv-loading v-if="!config.data.length">Loading</dv-loading>
        <div v-else class="content">
            <dv-scroll-board :config="config" style="width:80%;height:500px" />
        </div>
      </transition>
  </div>
</template>

<script>
export default {
    data(){
        return {
            config:{
                header: [],
                data: [],
                index: true,
                align: [],
                headerBGC:"#3077b1",
            },
            tableList:[]
        }
    },
    async created(){
        await this.delay(1500)
        this.getTableList()
    },
    methods:{
        delay(ms){
            return new Promise(resolve => setTimeout(resolve, ms));
        },
        async getTableList(){
            const res = await this.$http.get('/getTable')
            this.tableList = res.data.Lines_List
            this.config.header = ['疾病类型','挂号科室','患者性别','患者年龄','患者身高','患者体重','过敏史']
            this.config.data = res.data.Lines_List
            this.config.align = this.config.header.map(item => 'center')
            this.config.align.push('center')
        }
      
    }
}
</script>

<style scoped>
.content{
    display: flex;
    justify-content: center;
}
    .fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>