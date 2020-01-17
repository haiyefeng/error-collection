<template>
    <div class="topic">
        <header class="subject">
            <el-form v-if="isEdit" ref="subject" :model="errorDict.subject" inline>
                <el-input v-model="errorDict.subject.index" size="small" placeholder="输入题目" style="width:7%;"></el-input>
                <el-input type="textarea" autosize v-model="errorDict.subject.content" style="width:70%;"></el-input>
                <el-button type="primary" size="mini" icon="el-icon-plus" circle @click="addSubject"></el-button>
                <el-button type="danger" size="mini" style="margin:0" icon="el-icon-minus" circle @click="delSubject"></el-button>
            </el-form>
            <span v-else>
                {{errorDict.subject.index}}&nbsp;&nbsp;{{errorDict.subject.content}}
            </span>
        </header>
        <div>
        <error-option
        v-for="(item, index) in errorDict.options"
        :key="index"
        v-bind:option.sync="errorDict.options[index]"
        v-bind:index="index"
        v-bind:isEdit="isEdit"
        @add-option="addOption(errorDict.options, index)"
        @del-option="delOption(errorDict.options, index)"></error-option>
        </div>
    </div>
</template>

<script>
import Option from '@/components/errorOption'

export default {
    components: {
        'error-option': Option,
    },
    data() {
      return {
      }
    },
    props: ['errorDict', 'isEdit'],
    methods: {
        // 增加一道题
        addSubject() {
            this.$emit('add-subject');
        },
        // 减少一道题
        delSubject() {
            this.$emit('del-subject');
        },
        addOption(optionList, index) {
            optionList.push('sadsa');
        },
        delOption(optionList, index) {
            if (optionList.length > 1) {
                optionList.splice(parseInt(index), 1); 
            } else {
                this.$message.error("请至少保留一个选项");
            }
        }
    },
  }
</script>

<style scoped>
.subject {
    margin: 5px auto;
}
.topic {
   margin: 10px 2%; 
}
</style>
