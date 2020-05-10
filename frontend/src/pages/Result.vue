<template>
<div>
<el-button @click="submit_summary">按钮</el-button>
<div>
  <minder ref="minder" style="top:120px;bottom:50px;right:10px;"
  :importData="data"
  :style="isCollapse ? 'left: 90px' : 'left: 200px'"
  @exportData="exportData(data)"
  @minderChange="test"
  ></minder>
</div>
</div>
</template>
<script>
import { mapGetters, mapMutations } from 'vuex'

  export default {
    data () {
      return {
        data: {},
        new_data: {},
        chapter: '1',
        subjectTitle: '计算机网络',
      }
    },
    created() {
      this.getSummary();
    },
    mounted() {
    },
    computed: {
    ...mapGetters('main', ['isCollapse'])
    },
    methods: {
      submit_summary() {
        let data_dict = JSON.parse((this.new_data));
        data_dict.root.data.chapter = this.chapter;
        data_dict.root.data.subject_title = this.subjectTitle;
        let params = data_dict
        console.log(params);
        this.$api.editSummary(params).then(res =>{
          if (res.result) {
            console.log(res);
          }
          }).catch((err)=>{
          console.log(err);
          });
      },
      test(data){
        this.new_data = JSON.stringify(data)
        console.log(this.new_data)
      },
      exportData(data) {
        console.log(data)
      },
      getSummary() {
        this.$api.getSummary().then(res =>{
          if (res.result && JSON.stringify(res.data)!='{}') {
            this.data = res.data;
          }
          }).catch((err)=>{
          console.log(err);
          });
        },
    }
  }
</script>

<style scoped>
  #minder-container {
    width: 100%;
    height: 100%;
  }
</style>