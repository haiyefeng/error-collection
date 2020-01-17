<template>
    <div style="display:inline-block; width:49%;">
        <div v-if="isEdit">
            <el-form ref="form" inline>
                <el-input type="textarea"
                autosize
                v-model="inputValue"
                @input="changeValue"
                style="width:70%;"></el-input>
                <el-button type="primary" size="mini" icon="el-icon-plus" circle @click="addOption"></el-button>
                <el-button type="danger" size="mini" style="margin:0" icon="el-icon-minus" circle @click="delOption"></el-button>
            </el-form>
        </div>
        <div class="displayStatus" v-else>
            <span>
                {{indexToCode}}&nbsp;&nbsp;{{option}}
            </span>
        </div>
    </div>
</template>
<script>
  export default {
    data() {
      return {
        inputValue: ''
      }
    },
    created() {
      this.initValue();
    },
    computed: {
        indexToCode: function() {
            return String.fromCharCode(64 + parseInt(this.index) + 1);
        },
    },
    props: ['option', 'isEdit', 'index'],
    methods: {
      initValue() {
        this.inputValue = this.option;
      },
      changeValue() {
        console.log(this.inputValue);
        this.$emit('update:option', this.inputValue);
      },
    // 添加一个选项
      addOption() {
        this.$emit('add-option');
      },
    // 删除一个选项
      delOption() {
        this.$emit('del-option');
      },
    },
  }
</script>
<style scoped>
.displayStatus {
    margin: 5px 0;  
}
</style>
