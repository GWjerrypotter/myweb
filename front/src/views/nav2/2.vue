<template>
  <div>
    <div id="fixedBar" :class="{ fixedBar: isFixed, scrollBar: active }">
      <div class="logo" style="height: 80px">
        <p>许昌农村商业银行</p>
      </div>
      <div class="nav1">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          background-color="transparent"
          text-color="#fff"
          active-text-color="#fff"
          mode="horizontal"
          style="height: 80px"
          default-active="none"
          @select="handleSelect"
        >
          <el-menu-item index="1">菜单一</el-menu-item>
          <el-menu-item index="2">菜单二</el-menu-item>
          <el-menu-item index="3">菜单三</el-menu-item>
          <el-menu-item index="4">
            <a href="https://www.ele.me" target="_blank" style="text-decoration: none">菜单四</a>
          </el-menu-item>
        </el-menu>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      activeIndex: "1",
      activeIndex2: "1",
      isFixed: true, // bar浮动
      active: false, // 滚动后变化
      offsetTop: 0, // 触发bar浮动的阈值
      marginTop: 0, // 触发bar浮动的同时 给数据列表一个margin-top 防止列表突然上移 会很突兀
    };
  },
  mounted() {
    // 设置bar浮动阈值为 #fixedBar 至页面顶部的距离
    this.offsetTop = document.querySelector("#fixedBar").offsetTop;

    // 开启滚动监听
    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    handleScroll() {
      var scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (scrollTop > this.offsetTop) {
        this.isFixed = true;
        this.marginTop = document.querySelector("#fixedBar").offsetHeight + "px";
        this.active = true;
      } else {
        this.isFixed = true;
        this.marginTop = 0;
        this.active = false;
      }
    }
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll); // 离开页面 关闭监听 不然会报错
  }
};
</script>

<style scope>
body {
  margin: 0;
  padding: 0;
}
p {
  padding-top: 15%;
  margin: 0;
  vertical-align: middle;
  font-size: 16px;
  color: #fff;
}
div.logo {
  float: left;
  padding-left: 10%;
}
div.nav1 {
  float: right;
  padding-right: 10%;
  height: 61px;
}
.el-menu-item {
  font-size: 16px;
}
.el-menu.el-menu--horizontal {
  border-bottom: none;
}
.el-menu.el-menu--horizontal：focus {
  border-bottom: none !important;
}
.el-menu-item:hover {
  background-color: transparent !important;
}
.el-menu-item.is-active {
  border-bottom-color: transparent !important;
}
.fixedBar {
  /* padding-top: -10px; */
  position: fixed;
  top: 0;
  z-index: 999;
  width: 100%;
  background: rgba(21, 61, 236, 100);
  transition: background .4s, height .4s, top .4s;
  -moz-transition: background .4s, height .4s, top .4s;
  -webkit-transition: background .4s, height .4s, top .4s;
  -o-transition: background .4s, height .4s, top .4s;
  height: 80px;
}
.scrollBar {
  top: -10px;
  background: #0052d9;
  /* transition: background .4s, height .4s, top 1s;
  -moz-transition: background .4s, height .4s, top 1s;
  -webkit-transition: background .4s, height .4s, top 1s;
  -o-transition: background .4s, height .4s, top 1s; */
  height: 61px;
}
</style>