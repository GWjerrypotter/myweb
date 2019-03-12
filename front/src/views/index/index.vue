<template>
  <div>
    <v-nav></v-nav>
    <div class="block">
      <el-carousel trigger="click" height="500px" arrow="never">
        <el-carousel-item v-for="item in src" :key="item">
          <div class="outer">
            <video loop autoplay preload muted>
              <source :src="item" type="video/mp4">
            </video>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
    
    <div class="samury">
      <h1 class="title">{{ title }}</h1>
      <p>许昌魏都农村商业银行股份有限公司是在原许昌市魏都区农村信用合作联社基础上</p>
      <p>经过股份制改造由中国银行监督管理委员会批准成立的地方股份制金融机构</p>
      <p>是河南省第一批获银监会批准筹建的农商行、第二家农村商业银行、首家城区农村商业银行，也是许昌市第一家获准开业的农商行。</p>
      <br>
      <router-link to="/summary">
        <span class="gotosum">Learn More</span>
        <i class="el-icon-arrow-right"></i>
      </router-link>
    </div>
    
    <div class="bg1">
      <div class="content">
        <el-row :gutter="100">
          
          <el-col :span="8">
            <div class="grid-content bg-purple">
              <router-link to="/news" class="tonews">
                <div class="bgimg1"></div>
                <h2>农信新闻</h2>
                <p class="news_title">123</p>
                <span class="lm">Learn More<i class="el-icon-arrow-right"></i></span>
              </router-link>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content bg-purple">
              <router-link to="/anns" class="tonews">
                <div class="bgimg1"></div>
                <h2>农信新闻</h2>
                <p class="news_title">123</p>
                <span class="lm">Learn More<i class="el-icon-arrow-right"></i></span>
              </router-link>
              <el-table
                :data="tableData"
                style="width: 100%">
                <el-table-column
                  prop="doc_title"
                  width="100">
                </el-table-column>
                <el-table-column
                  prop="publish_time"
                  width="180">
                </el-table-column>
              </el-table>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content bg-purple">
              <router-link to="/others" class="tonews">
                <div class="bgimg1"></div>
                <h2>农信新闻</h2>
                <p class="news_title">123</p>
                <span class="lm">Learn More<i class="el-icon-arrow-right"></i></span>
              </router-link>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="extra">
      <ul>
        <li v-for="item in list1">
          {{ item.doc_title }}
        </li>
      </ul>
    </div>
    <div style="height: 1000px"></div>
  </div>
</template>

<script>
import { getBrief } from '@/api/index'
import nav from "../nav/index.vue";
export default {
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      src: [
        "https://www.tencent.com/video/bannerbg1.mp4",
        "https://www.tencent.com/video/bannerbg2.mp4"
      ],
      title: "服务三农，相融共生",
      tableData: [],
      list1: [],
    };
  },
  components: {
    "v-nav": nav
  },
  mounted() {
    this.getbrief()
  },
  methods: {
    getbrief() {
      getBrief().then(response => {
        console.log(response)
        this.tableData = response.data.results
        this.list1 = response.data.results
      })
      .catch((err)=>{
            console.log(err);
        })
    }
  }
};
</script>

<style scope>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
video {
  height: 500px;
  top: 0;
  position: absolute;
  /* width: 100%; */
  display: inline-block;
}
h1 {
  font-size: 50px;
  color: red
}
h2 {
  left: 100px;
  position: absolute;
}
.el-col {
  min-width: 300px;
}
.el-col-8 {
  min-width: 300px;
}
.tonews {
  width: inherit;
  height: 300px;
  display: block;
  position: relative;
}
.news_title {
  top: 84px;
  position: absolute;
}
.lm {
  bottom: 40px;
  position: absolute;
  color: #ee6a59;
}
.bg1 {
  background-image: url(https://demo.budflare.com/streetfood/wp-content/uploads/sites/2/2018/10/sf-3.jpg);
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
}
a {
  text-decoration: none;
}
.gotosum {
  color: green;
  font-size: 20px;
}
i {
  size: 15px;
}
.samury {
  margin: 5%;
  text-align: center;
}
.samury p {
  font-size: 25px;
  padding: 0;
  margin: 10px 0 5px 0;
  color: black;
}
.content {
  margin-top: 5%;
  margin-left: 10%;
  margin-right: 10%;
}
.bgimg1 {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  background-image: url(http://www.tencent.com/images/index/news_bg_1.png);
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  height: 600px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>