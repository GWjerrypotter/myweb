<template>
  <div>
    <div id="fixedBar" :class="{ fixedBar: isFixed, scrollBar: active }">
      <div class="logo">
        <p style="color: #fff">许昌农村商业银行</p>
      </div>
      <div class="nav1">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          background-color="transparent"
          text-color="#fff"
          active-text-color="#fff"
          mode="horizontal"
          style="height: 59px"
          default-active="none"
          @select="handleSelect"
        >
          <el-menu-item index="1"><i class="c_line" style="height: 5px, float: top"></i>菜单一</el-menu-item>
          <el-menu-item index="2">菜单二</el-menu-item>
          <el-menu-item index="3">菜单三</el-menu-item>
          <el-menu-item index="4">
            <a href="https://www.ele.me" target="_blank" style="text-decoration: none">菜单四</a>
          </el-menu-item>
        </el-menu>
      </div>
    </div>
    <!-- <div class="outer" id="video">
      <video src="https://www.tencent.com/video/bannerbg1.mp4" loop autoplay preload muted></video>
    </div> -->
    <div style="height: 1000px"></div>
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
div.logo {
  float: left;
  padding-left: 10%;
}
div.nav1 {
  float: right;
  padding-right: 10%;
  height: 61px;
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
  height: 200px;
  background: rgba(0, 0, 0, 0);
  transition: background 1s;
  -moz-transition: background 1s;
  -webkit-transition: background 1s;
  -o-transition: background 1s;
}
.scrollBar {
  background: #0052d9;
  transition: background 1s;
  -moz-transition: background 1s;
  -webkit-transition: background 1s;
  -o-transition: background 1s;
}
.outer {
  height: inherit;
}
/* video {
  height: 600px;
  top: 0;
  position: absolute;
  width: 100%;
} */
</style>