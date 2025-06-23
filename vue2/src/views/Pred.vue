<template>
  <div class="pred-container">
    <div class="left">
        <div class="title">
          <img src="../assets/logo.png" style="width:80px;height:80px;" alt="">
           病情初步预测
        </div>
        <br/>
        <div>
          <span style="font-size: 1.5em;color: azure;">病情描述：</span>&nbsp;&nbsp;&nbsp;
          <input v-model="textInput" style="width:200px;height:30px;text-align: center;" placeholder="输入疾病描述" />
        </div>
        <br/>
          <button @click="submitText" style="width:200px;height:40px;">提交</button>
    </div>
    
    <div class="right">
      <div class="top">
        <dv-decoration-11 style="width:450px;height:80px;text-align: center;color:azure;font-weight: bold;">小贴士：仅为机器预测，如有任何身体不适，请及时到有关医院就医。</dv-decoration-11>
      </div>
        <br/>
        <br/>
        <br/>
      <div class='content' style="width:450px;height:60px;text-align: center;color:azure;font-weight: bold;">
        <dv-decoration-11>预测结果</dv-decoration-11>
      </div>
      <br/>
      <dv-border-box-8 :reverse="true" style="width:450px; height:100px;">
        <div style="width:100%; height:100%; display:flex; justify-content:center; align-items:center; text-align:center; color:azure; font-weight:bold;font-size: 18px;">{{ result }}</div>
      </dv-border-box-8>           
    </div>
      <div class="top bottom">

            <div class="content">
              <div class="title">
              </div>
             
            </div>
      
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Pred',
  data() {
    return {
      textInput: "",
      result: "暂无信息",
    };
  },
  created(){

  },
  methods: {
    async submitText() {
      if (!this.textInput) {
        this.result = "请输入描述";
        return;
      }

      try {
        const res = await this.$http.post("/getPred", {
          text: this.textInput,
        });
        this.result = res.prediction;
      } catch (e) {
        this.result = "预测失败，请检查后端服务";
        console.error(e);
      }
    },
  },
  components: {
    
  }
}
</script>

<style lang="less" scoped>
  .button{
    width: 100%;
    height: 30px;
    display: flex;
    justify-content: center;
  }
  button{
    width: 80%;
    height: 100%;
    background: #26fffd;
    color:rgb(0, 0, 0);
    border-radius: 15px;
    
  }
  .pred-container{
    display: flex;
    width: 100%;
    height: 100vh;
    .left{
      width: 800px;
      display: flex;
      flex-direction: column;
      align-items: center;
      .title{
        color:#26fffd;
        margin-top: 80px;
        font-size: 38px;
        font-weight: bold;
      }
      .form{
        margin-top: 35px;
        .form-group{
          display: flex;
          align-items: center;
          margin-bottom: 15px;
          .form-label{
            margin-right: 25px;
            font-size: 18px;
            color:#fff;
          }
          .form-control input{
            border-radius: 15px;
            background: #d3dcf7;
            border: none;
            outline: none;
            padding: 0 5px;
            height: 25px;
            width: 200px;
          }
          .form-control select{
            border-radius: 15px;
            background: #d3dcf7;
            border: none;
            outline: none;
            padding: 0 5px;
            height: 25px;
            width: 210px;
          }
        }
      }
    }
    .right{
      flex: 1;
      .top{
        margin-top: 70px;
        width: 80%;
        // height: 500px;
        .content{
          padding:15px 25px;
          .title{
            display: flex;
            justify-content: center;
            align-items: center;
            color:#fff;
            font-weight: bold;
            font-size: 18px;
          }
          .word{
            font-size: 20px;
            color:orange;
            margin-top:15px;
            padding:0 20px;
            background: linear-gradient(to right, orange, #26fffd);
            -webkit-background-clip: text; /* 使用文本作为背景剪辑 */
            color: transparent; /* 隐藏文字本身的颜色 */
            display: inline-block; /* 确保渐变应用在文字上 */
          }
        }
      }
      .bottom{
        margin-top: 30px;
        width: 80%;
        height: 200px;
      }
    }
  }
</style>
