<template>
  <div class="home">
    <transition name="fade" mode="out-in">
      <dv-border-box-10>
        <div class="naca">
          <div class="index-header" style="margin-top: 5px">
            <div>
              <dv-decoration-10 style="width: 450px; height: 1px; margin-bottom: 45px" />
              <dv-decoration-8 style="width: 180px; height: 50px" :color="['#568aea', '#000000']" />
              <div style="
                  width: 150px;
                  color: #eeecec;
                  font-size: 18px;
                  padding: 0 15px;
                  font-weight: bold;
                ">
                可视化化平台
              </div>
              <dv-decoration-8 :reverse="true" style="width: 180px; height: 50px" :color="['#568aea', '#000000']" />
              <dv-decoration-10 style="
                  width: 450px;
                  height: 1px;
                  transform: rotateY(180deg);
                  margin-bottom: 45px;
                " />
            </div>
            <dv-decoration-5 style="width: 10%; height: 20px" :color="['#568aea', '#000000']" />
          </div>

          <div class="index-content">
            <div class="left">
              <div class="left-1" style="">

                <dv-border-box-12>
                  <div style="padding: 5px">
                    <div class="title" style="margin-top: 5px">
                      各年龄段患病占比
                    </div>

                    <div ref="firstMain" style="width: 100%; height: 120px"></div>
                  </div>
                </dv-border-box-12>
                <dv-border-box-8>
                  <div style="padding: 5px;padding-bottom:30px">
                    <div class="title" style="margin-top: 1px">疾病类型分布</div>
                    <div style="width: 100%; height: 110px; overflow: hidden;">
                      <dv-capsule-chart :config="Disease_type" style="width:90%;height: 100px;" />
                    </div>
                  </div>
                </dv-border-box-8>

                <dv-border-box-3>
                  <div style="padding: 15px">
                    <div class="title" style="margin-top: 5px">病例列表</div>
                    <div class="row_list" style="">
                      <ul class="cases_list" style="width: 100%;height: 159px;overflow: auto;">
                        <li style="font-size: 15px;">
                          <div>求诊类型</div>
                          <div>挂号科室</div>
                          <div>性别</div>
                          <div>年龄</div>
                          <div>身高</div>
                          <div>体重</div>
                          <div>过敏史</div>
                        </li>
                        <li v-for="record in Lines">
                          <div>{{ record[0] }}</div>
                          <div>{{ record[1] }}</div>
                          <div>{{ record[2] }}</div>
                          <div>{{ record[3] }}</div>
                          <div>{{ record[4] }}</div>
                          <div>{{ record[5] }}</div>
                          <div>{{ record[6] }}</div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </dv-border-box-3>
              </div>
            </div>

            <div class="cents">
              <div class="above">
                <div class="aboveOne">
                  <div style="padding: 15px">
                    <div class="title">疾病数据信息</div>
                    <div style="
                        display: flex;
                        flex-direction: column;
                        width: 100%;
                        height: 120px;
                        color: #eeecec;
                      ">
                      <div style="display: flex; flex: 1">
                        <dv-decoration-11 style="height:60px;text-align: center;">数据数量：{{ Center_Display[0]
                        }}</dv-decoration-11>
                        <dv-decoration-11 style="height:60px;text-align: center;">最多疾病类型：{{ Center_Display[1]
                        }}</dv-decoration-11>
                        <dv-decoration-11 style="height:60px;text-align: center;">求诊最多科室：{{ Center_Display[2]
                        }}</dv-decoration-11>
                      </div>
                      <div style="display: flex; flex: 1">
                        <dv-decoration-11 style="width: 150px;height:60px;text-align: center;">最大患者年龄：{{ Center_Display[3]
                        }}</dv-decoration-11>
                        <dv-decoration-11 style="width: 150px;height:60px;text-align: center;">最小患者年龄：{{ Center_Display[4]
                        }}</dv-decoration-11>
                        <dv-decoration-11 style="width: 150px;height:60px;text-align: center;">热门医院：{{ Center_Display[5]
                        }}</dv-decoration-11>
                      </div>
                    </div>
                  </div>
                  <div style="padding: 15px">
                    <div class="title" style="margin-top: -30px">
                      男女患病对比
                    </div>
                    <div class="content">
                      <dv-active-ring-chart v-if="isDataLoaded" :config="man_prop" style="width:150px; height:100px" />
                      <dv-water-level-pond v-if="isDataLoaded" :config="gender_ratio" style="width:150px;height:100px" />
                      <dv-active-ring-chart v-if="isDataLoaded" :config="woman_prop" style="width:150px;height:100px" />
                    </div>
                  </div>
                </div>
                <div class="aboveTwo">
                  <dv-border-box-1>
                    <div style="padding: 15px">
                      <div class="title" style="margin-top: 5px">
                        医院科室环形图
                      </div>
                      <div ref="secondMian" style="width: 100%; height: 110px"></div>
                    </div>
                  </dv-border-box-1>
                  <dv-border-box-10>
                    <div style="padding: 5px">
                      <div class="title" style="margin-top: 5px">
                        疾病关键词云图
                      </div>
                      <div ref="thirdMain" style="width: 400px; height: 90px"></div>
                    </div>
                  </dv-border-box-10>

                </div>
              </div>
              <div class="below">

                <dv-border-box-13>
                  <div style="padding: 7px">
                    <div class="title" style="margin-top: 5px">
                      患者身高体重平均数图
                    </div>
                    <div ref="lastMain" style="width: 100%; height: 200px; margin-top: 25px"></div>
                  </div>
                </dv-border-box-13>

              </div>
            </div>
          </div>
        </div>
      </dv-border-box-10>
    </transition>
  </div>
</template>

<script>
import $ from "jquery";
import LeftTop from "@/components/LeftTop.vue";
import { reactive } from "vue";
// import { set } from "vue/types/umd.js";
function formatter(number) {
  const numbers = number.toString().split("").reverse();
  const segs = [];

  while (numbers.length) segs.push(numbers.splice(0, 3).join(""));

  return segs.join(",").split("").reverse().join("");
}
export default {
  name: "Index",
  data() {
    return {
      isDataLoaded: false,
      currentIndex: 0,
      pieData: [],
      Disease_type: {
      },
      Lines: [],
      Center_Display: {
      },
      man_prop: {
        lineWidth: 20,
        radius: "50%",
        activeRadius: "60%",
        activeTimeGap: 2000,
        digitalFlopStyle: {
          fontSize: 12,
        },
        data:[],
      },
      gender_ratio: {
        shape: "roundRect",
        data: [],
      },
      woman_prop: {
        lineWidth: 20,
        radius: "50%",
        activeRadius: "60%",
        activeTimeGap: 2000,
        digitalFlopStyle: {
          fontSize: 12,
        },
        data: [],
      },
      department_sum: [],
      wordsets: [],
      avg_chart: [],
    };
  },

  components: {
    LeftTop,
  },

  methods: {
    setPieData() {
      $(document).ready(() => {
        var chartDom = this.$refs.firstMain;
        var myChart = this.$echarts.init(chartDom);
        myChart.dispatchAction({
          type: 'downplay',
          seriesIndex: 0,
          dataIndex: this.currentIndex
        })
        this.currentIndex = (this.currentIndex + 1) % this.pieData.length
        myChart.dispatchAction({
          type: 'highlight',
          seriesIndex: 0,
          dataIndex: this.currentIndex
        })
        var option = {
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}:{c} ({d}%)'
          },
          toolbox: {
            show: true
          },
          calculable: true,
          legend: {
            orient: 'vertical',
            icon: 'circle',
            left: 0,
            x: "center",
            data: this.pieData.map((item) => item.name),
            textStyle: {
              color: '#fff'
            }
          },
          series: [
            {
              name: '年龄占比',
              type: 'pie',
              radius: [20, 50],
              roseType: 'area',
              center: ['50%', '55%'],
              label: {
                show: true,
              },
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  label: {
                    show: true,
                    fontWeight: 'bold'
                  },
                }
              },
              data: this.pieData
            }
          ]
        };
        option && myChart.setOption(option);
      })
    },
    getSeriesData(){
      const series = [];
      this.department_sum.forEach((item, index) => {
        if(index<5){
        series.push({
          name: item.name,
          type: 'pie',
          clockWise: false,
          hoverAnimation: false,
          radius: [73 - index*15 + "%", 68 - index*15 + "%"],
          center: ["50%","50%"],
          label: {
            show: false,
          },
          data: [
            {
              value: item.value,
              name: item.name
            },
            {
              value: 3,
              itemStyle: {
                color: "rgba(0,0,0,0)",
                borderWidth: 0,
              },
              tooltip: {
                show: false,
              },
              hoverAnimation: false,
            }
          ],
        })};
      });
      return series;
    },
    Rotating_Bar(arr) {
      const first = arr.shift()
      arr.push(first)
    },
    setCircle(){
      $(document).ready(()=>{
        var newData = this.department_sum;
        this.Rotating_Bar(newData);
        this.department_sum = newData;
        var chartDom = this.$refs.secondMian;
        var myChart = this.$echarts.init(chartDom);
        var option = {
          legend: {
            show: true,
            icon: "circle",
            top: "8%",
            left: "10%",
            data: this.department_sum.map((item) => item.name),
            width: -5,
            itemWidth: 10,
            itemHeight: 10,
            itemGap: 6,
            textStyle: {
              fontSize: 12,
              lineHeight: 5,
              color: "#ffffff",
            }
          },
          tooltip: {
            show: true,
            trigger: "item",
            formatter: "{b}<br>{c}({d}%)",
          },
          yAxis: [
            {
              type: "category",
              inverse: true,
              axisLine: {
                show: false,
              },
            },
          ],
          xAxis: [
            {
              show: true,
            },
          ],
          series: this.getSeriesData()
        };
        option && myChart.setOption(option);
      });
    },
    setDisease_type() {
      // 深拷贝一份，避免直接改原数组
      let newData = [...this.Disease_type.data]
      // 滚动数据
      this.Rotating_Bar(newData)
      // 设置新的配置
      this.Disease_type = {
        data: newData,
        showValue: true
      }
    },
    randomColor() {
      const r = Math.floor(Math.random() * 255);
      const g = Math.floor(Math.random() * 255);
      const b = Math.floor(Math.random() * 255);
      return `rgb(${r},${g},${b})`
    },
    setWord_plot() {
      var chartDom = this.$refs.thirdMain;
      var myChart = this.$echarts.init(chartDom);
      const wordData = this.wordsets.map(word => ({
        ...word,  // 展开原有属性（name, value等）
        textStyle: {
          color: this.randomColor() // 每个词单独随机颜色
        }
      }));
      var option = {
        series: {
          type: "wordCloud",
          sizeRange: [8,20],
          gridSize: 1,
          rotationRange: [0,0],
          layoutAnimation: true,
          emphasis: {
            textStyle:{
              fontWeight: "bold",
              color: "#fff"
            },
          },
          data: wordData      
        },
      };
      option && myChart.setOption(option);
    },
    setAvg_plot() {
     $(document).ready(()=>{
      var newData = this.avg_chart
      this.Rotating_Bar(newData.xData)
      this.Rotating_Bar(newData.yData1)
      this.Rotating_Bar(newData.yData2)
      this.avg_chart = newData
      var chartDom = this.$refs.lastMain;
      var myChart = this.$echarts.init(chartDom);
      var option = {
        tooltip:{
          trigger: 'axis',
          label: {
            show: true,
            backgroundColor: '#7B7DDC',
          }
        },
        dataZoom:[
          {
            type: 'slider',
            start: 0,
            end: 80,
            show: false,
          },
        ],
        legend: {
          data: ['身高', '体重'],
          textStyle: {
            color: '#B4B4B4',
          },
          top: "0%",
        },
        grid: {
          x: "8%",
          width: "85%",
          height: "87%",
          y: "4%",
        },
        xAxis: {
          data: this.avg_chart.xData,
          axisLine: {
            lineStyle: {
              color: "#B4B4B4",
            },
          },
          axisLabel: {
            show: true,
            interval: 0,
          },
          axisTick:{
            show: false,
          },
        },
        yAxis: [
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#B4B4B4",
              },
            },
            axisLabel: {
              formatter: "{value}",
            },
          },
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#B4B4B4",
              },
            },
            axisLabel: {
              formatter: "{value}",
            },
          }
        ],
        series: [
          {
            name: "身高",
            type: "line",
            smooth: true,
            showAllSymbol: true,
            symbol: "emptyCircle",
            symbolSize: 8,
            yAxisIndex: 1,
            itemStyle: {
              normal:{
                barBorderRadius: 5,
                color: new this.$echarts.graphic.LinearGradient(0,0,0,1,[
                  {offset: 0, color:"#5C4033"},
                  {offset: 1, color:"#FAEBD7"},
                ]),
              },
            },
            data: this.avg_chart.yData1
          },
          {
            name: "体重",
            type: "bar",
            barWidth: "60%",
            itemStyle: {
              normal:{
                barBorderRadius: 5,
                color: new this.$echarts.graphic.LinearGradient(0,0,0,1,[
                  {offset: 0, color:"#082e53"},
                  {offset: 1, color:"white"},
                ]),
              },
            },
            data: this.avg_chart.yData2
          },
        ]
      };
      option && myChart.setOption(option);
     })
    },
  },


  async created() {
    $(document).ready(async () => {
      setInterval(() => {
        this.setPieData()
      }, 1000);
      setInterval(() => {
        this.setDisease_type()
        this.setCircle()
        this.setWord_plot()
        this.setAvg_plot()
      }, 1500);
    })
  },

  async mounted() {
    const res = await this.$http.get("/getHomedata")
    this.pieData = res.data.pieData
    this.Disease_type.data = res.data.Disease_type_data
    this.Lines = res.data.Lines
    this.Center_Display = res.data.Center_Display
    this.department_sum = res.data.Department_Summary
    this.man_prop.data = res.data.man_prop
    this.gender_ratio.data = res.data.gender_ratio
    this.woman_prop.data = res.data.woman_prop
    this.wordsets = res.data.Wordset
    this.avg_chart = res.data.Average_chart
    this.isDataLoaded = true
    console.log(this.avg_chart)
  },
};
</script>

<style lang="less" scoped>
.loading {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.cent-1-content {
  padding: 20px;
  display: flex;
}

.right-content {
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.right-content div {
  display: flex;
  font-size: 15px;
  align-items: center;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.cents {
  display: flex;
  flex-direction: column;
}

.above {
  display: flex;
}

.aboveOne {
  display: flex;
  flex-direction: column;
}

.aboveTwo {
  display: flex;
  flex-direction: column;
}

.cent {
  width: 850px;
  height: 300px;
}

.cent-1 {
  margin: 10px;
  color: aliceblue;
  width: 500px;
  height: 220px;
  /* background-color: rgb(26, 26, 133); */
}

.left {
  display: flex;
  flex-direction: column;
}

.left-1 {
  margin: 15px;
  color: aliceblue;
  width: 550px;
  display: flex;
  flex-direction: column;
}

.left-2 {
  margin: 15px;
  color: aliceblue;
  width: 530px;
  display: flex;
  flex-direction: column;
}

.naca {
  // padding: 35px 15px 0 15px;
  box-sizing: border-box;
  width: 100%;
  // height: 40rem;
  display: flex;
  flex-direction: column;
}

.naca .index-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.naca .index-header div {
  display: flex;
  justify-content: center;
  align-items: center;
}

.naca .index-content {
  display: flex;
  justify-content: center;
  align-items: center;
}

.bg {
  width: 100%;
  height: 45rem;
  background-color: black;
  position: relative;
}

.title {
  color: #3f96a5;
  font-size: 18px;
  margin-top: -20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-weight: bold;
}

.content {
  display: flex;
  align-items: center;
}

.content-word {
  width: 140px;
  height: 130px;
  background: #11193e;
  border-radius: 40px;
  border: 1px solid #3d3d3d;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.content-word-item {
  margin-left: 19px;
  margin-bottom: 10px;

  img {
    width: 20px;
    height: 20px;
  }
}

.content-word-item-title {
  font-size: 18px;
}

.content-word-item-content {
  margin-top: 5px;

  display: flex;
  align-items: center;
}

.row_list {
  list-style: none;
}

.cases_list::-webkit-scrollbar {
  display: none;
}

.cases_list li {
  display: grid;
  -ms-grid-columns: 80px 120px 60px 60px 60px 50px 50px;
  grid-template-columns: 80px 120px 60px 60px 60px 50px 50px;
  cursor: pointer;
  margin-left: 23px;
  text-align: center;
  line-height: 30px;
  color: rgb(238, 236, 236);
}

.list_time {
  height: 30px;
  overflow: auto;
}

.list_time::-webkit-scrollbar {
  display: none;
}
</style>