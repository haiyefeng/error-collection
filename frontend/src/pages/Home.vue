<template>
  <div class="homecontainer">
    <div class="fixbtn" :style="isCollapse ? 'left: 10%' : 'left: 16%'">
      <select-box :modelName="modelName"></select-box>
      <el-button @click="changeEdit" type="primary" icon="el-icon-edit">{{edit}}</el-button>
    </div>
    <div class="errorsubject" :style="isCollapse ? 'left: 10%' : 'left: 15%'">
      <error-subject v-for="(item, index) in errorList" :key="index" v-bind:errorDict="item" v-bind:isEdit="isEdit" @add-subject="addSubject(index)" @del-subject="delSubject(index)"></error-subject>
    </div>
  </div>
</template>

<script>
import Subject from '@/components/errorSubject'
import { mapGetters, mapMutations } from 'vuex'
import SelectBox from '@/components/selectBox'

export default {
  components: {
    'error-subject': Subject,
    'select-box': SelectBox,
  },
  data() {
    return {
      modelName: 'Mistake',
      errorList: [],
      edit: '编辑',
      isEdit: false,
    }
  },
  computed: {
    ...mapGetters('main', ['isCollapse'])
  },
  mounted() {
    this.getErrorList();
  },
  methods: {
    getErrorList() {
      this.$api.getMistake().then(res =>{
        if (res.result) {
          this.errorList = res.data;
        }
      }).catch((err)=>{
        console.log(err);
      })
    },
    changeEdit() {
      if (this.isEdit) {
        this.isEdit = !this.isEdit;
        this.edit = '编辑';
        console.log(this.errorList);
        let params = this.errorList;
        this.$api.createMistakes(params).then(res =>{
          if (res.result) {
            console.log('ok');
          }
        }).catch((err)=>{
          console.log(err);
        })
      } else {
        this.isEdit = !this.isEdit;
        this.edit = '保存';
      }
    },
    addSubject(index) {
      this.errorList.push({subject: {index: this.errorList.length + 1, content: ''}, options: ['']})
    },
    delSubject(index) {
      if (this.errorList.length > 1) {
        this.errorList.splice(parseInt(index), 1); 
      } else {
        this.$message.error("请至少保留一个选项");
      }
    },
  }
}
</script>

<style scoped>
.homecontainer {
  height: 100%;
}
.fixbtn {
  position: fixed;
  top: 6%;
}
.errorsubject {
    position: absolute;
    /*绝对定位*/
    top: 15%;
    right: 0;
    bottom: 30px;   
    overflow-y: auto;/*显示y轴滚动条*/
    overflow-x: hidden;/*隐藏x轴滚动条*/   
}
</style>
