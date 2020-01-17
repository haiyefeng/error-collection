<template>
<div>
  <minder ref="minder" style="top:50px;bottom:50px;right:10px;"
  :importData="data"
  :style="isCollapse ? 'left: 90px' : 'left: 200px'"
  @exportData="exportData(data)"
  @minderChange="test"
  ></minder>
</div>
</template>
<script>
import { mapGetters, mapMutations } from 'vuex'

  export default {
    data () {
      return {
        data: {},
        importData: {
            "data": { "text": "Design project", "id": 2 },
            "children": [
                { 
                    "data": { "text": "Designsy", "id": 3 },
                    "children": [
                        { 
                          "data": { "text": "Designsy", "id": 4 },
                          "children": [
                            { "data": { "text": "Designsy", "id": 5 } },
                            { "data": { "text": "Designsy", "id": 5 } },
                            { "data": { "text": "Designsy", "id": 5 } },
                          ]
                        },
                        { "data": { "text": "Designsy", "id": 5 } },
                        { "data": { "text": "Designsy", "id": 62 } },
                        { "data": { "text": "Designsy", "id": 73 } },
                        { "data": { "text": "Designsy", "id": 84 } }
                    ]
                },
                { "data": { "text": "Designsy", "id": 9 } },
                { "data": { "text": "Designsy", "id": 102 } },
                { "data": { "text": "Designsy", "id": 113 } },
                { "data": { "text": "Designsy", "id": 124 } }
            ]
        },
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
      test(data){
        console.log(data)
      },
      exportData(data) {
        console.log(data)
      },
      getSummary() {
        this.$api.getSummary().then(res =>{
          if (res.result) {
            this.data = res.data;
            console.log(this.data);
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