<template>
    <el-container>
      <app-aside></app-aside>
      <container></container>
    </el-container>
</template>

<script>
    import Aside from '@/components/layout/leftMenu'
    import Container from '@/components/layout/container'

    export default {
        name: 'App',
        components: {
            'container': Container,
            'app-aside': Aside,
        },
        methods: {
        },
        data() {
          return {
          }
        },
    }
</script>
<style scoped>
.el-container {
  width: 100%;
  height: 100%;
};
</style>
