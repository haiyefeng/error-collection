<template>
    <el-container :style="isCollapse ? 'width: calc(100% - 80px)' : 'width: calc(100% - 210px)'">
        <app-header>Header</app-header>
        <el-main>
            <router-view/>
        </el-main>
        <app-footer></app-footer>
    </el-container>
</template>

<script>
    import Header from '@/components/layout/header'
    import Footer from '@/components/layout/Footer'
    import { mapGetters, mapMutations } from 'vuex'

    export default {
        name: 'container',
        mounted() {
        },
        computed: {
        ...mapGetters('main', ['isCollapse'])
        },
        components: {
            'app-header': Header,
            'app-footer': Footer,
        },
    }
</script>

<style scoped>
  .el-main {
    background-color:#F0F8FF;
    color: #333;
    height: calc(100% - 80px);
  }
  .el-container {
    display: inline-block;
    height: 100%;
  }
</style>