<template>
<div class="selectContainer">
    <span>科目名称：</span>
    <el-select v-model="subject" placeholder="请选择科目" style="width:150px;margin-right:10px;">
    <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
    </el-option>
    </el-select>
    <span>第</span>
    <el-select v-model="chapter" placeholder="——" style="width:60px;">
    <el-option
        v-for="item in chapterList"
        :key="item.value"
        :label="item.label"
        :value="item.value">
    </el-option>
    </el-select>
    <span style="margin-right:10px;">章</span>
</div>
</template>

<script>
  export default {
    props: ['modelName'],
    data() {
      return {
        chapterList: [{
          value: '选项1',
          label: '1',
        },
        ],
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        subject: '',
        chapter: '',
      }
    },
    mounted() {
        let params = {model: this.modelName}
        console.log(params);
        this.$api.selectInfo(params).then(res =>{
        if (res.result) {
          console.log('2132')
        }
        }).catch((err)=>{
            console.log(err);
        });
    },
    methods: {
    },
  }
</script>

<style scoped>
.selectContainer{
    display: inline-block;
}
</style>
