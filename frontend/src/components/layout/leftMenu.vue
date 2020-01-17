<template>
<el-aside :style="isCollapse ? 'width: 70px': 'width: 200px'" style="background-color:#F0F8FF;">
  <header style="position:fixed;top:5%;left:0.5%;">
    <div>导航栏</div>
  </header>
  <div style="position:absolute;top:12%;bottom:10%;
      height: 70%;
			width: 200px;
			overflow: hidden;
			margin: 20px auto;">
  <div style="height: 100%;
			width: 220px;
			overflow-y: auto;
			overflow-x: hidden;">
    <el-menu
      router
      :collapse-transition="false"
      style="min-width:70px;"
      default-active="home"
      background-color="#F0F8FF"
      text-color="#fff"
      active-text-color="#ffd04b"
      class="el-menu-vertical-demo"
      :collapse="isCollapse">
      <el-menu-item index="/">
        <i class="el-icon-document"></i>
        <span slot="title">导航一</span>
      </el-menu-item>
      <el-menu-item index="/test/">
        <i class="el-icon-reading"></i>
        <span slot="title">导航二</span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-menu"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item>
    </el-menu>
  </div>
  </div>
  <footer style="position:fixed;bottom:5%;left:1.5%;">
    <i :class="iconName" @click="changeCollapse"></i>
  </footer>
</el-aside>
</template>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
  }
</style>

<script>
  import { mapGetters, mapMutations } from 'vuex'

  export default {
    props: [],
    data() {
      return {
        iconName: 'el-icon-s-unfold',
      };
    },
    computed: {
        ...mapGetters('main', ['isCollapse'])
    },
    methods: {
        changeCollapse() {
          if (this.isCollapse) {
            this.iconName = 'el-icon-s-fold';
          } else {
            this.iconName = 'el-icon-s-unfold';
          }
          let isCollapse = !this.isCollapse
          this.$store.commit('main/setIsCollapse', isCollapse)
          // 保证菜单完全收缩或者拉伸后，再给window添加resize事件
          setTimeout(() => {
            let resizeEvent = new Event('resize')
            window.dispatchEvent(resizeEvent)
          }, 100)
        },
    }
  }
</script>

<style scoped>
  .el-aside {
    float: left;
    background-color: #D3DCE6;
    margin-right: 10px;
    color: #333;
    height: 100%;
  }
  .el-row h5{
    text-align: center;
  }
i:hover {
    color: aqua;
  }
</style>
