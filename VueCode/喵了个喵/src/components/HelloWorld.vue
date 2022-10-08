<template>
<h1>喵了个喵</h1>
  <div class="box">
	  	
    <!-- 上 -->
    <div class="top-box">
      <div class="card-box">
        <div class="card" @click="selectedCard(item, index, $event)" v-for="(item, index) in allCardList" :key="index" :style="{left: item.left, top: item.top}">
          <!-- {{item.id}} -->
          <i :class="item.icon"></i>
        </div>
      </div>
    </div>
    <hr>
    <!-- 下 -->
    <div class="selected-card-box">
      <div class="selected-card" v-for="(item, index) in selectedCardList" :key="index">
        <!-- {{item.id}} -->
        <i :class="item.icon"></i>
      </div>
    </div>
    <div class="btn">
      <el-button @click="initData()" type="primary">重新开始</el-button>
      <el-button @click="backCard()" type="primary">撤回</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      positionList: [],  //  定位数组
      allCardList: [
        /* {id: 1, picIndex: 1, icon: 'el-icon-platform-eleme', left: '0px', top: '0px'},
        {id: 2, picIndex: 1, icon: 'el-icon-platform-eleme', left: '50px', top: '0px'}, */
      ],  // 所有待选择的卡片list
      selectedCardList: [],  // 已选择的卡片list
      currentSelectedCard: {},  // 当前选中的卡片
      selectHistory: [],  // 记录已选择的卡片list，方便撤回操作
      iconList: [
        {picIndex: 0, icon: 'el-icon-s-flag'},
        {picIndex: 1, icon: 'el-icon-platform-eleme'},
        {picIndex: 2, icon: 'el-icon-delete-solid'},
        {picIndex: 3, icon: 'el-icon-s-tools'},
        {picIndex: 4, icon: 'el-icon-user-solid'},
        {picIndex: 5, icon: 'el-icon-warning'},
        {picIndex: 6, icon: 'el-icon-picture'},
        {picIndex: 7, icon: 'el-icon-upload'},
        {picIndex: 8, icon: 'el-icon-message-solid'},
        {picIndex: 9, icon: 'el-icon-video-camera-solid'},
        {picIndex: 10, icon: 'el-icon-s-platform'}
      ],  // 图标类型数组
    }
  },
  created() {
    this.initData()
  },
  methods: {
    // 撤回
    backCard() {
      console.log(this.allCardList);
      console.log(this.selectHistory);
      if (this.selectHistory.length > 0) {
        let backItem = this.selectHistory[this.selectHistory.length - 1]
        this.allCardList.push(backItem)
        this.allCardList.sort((a, b)=>{
          return a.id - b.id
        })
        this.selectHistory = this.selectHistory.filter(item=>{
          return item.id != backItem.id
        })
        this.selectedCardList = this.selectedCardList.filter(item=>{
          return item.id != backItem.id
        })
      } else {
        alert('没有可以撤回的卡片了！')
      }
      
    },
    // 选择卡片
    selectedCard(item, index, event) {
      console.log(item, index, event.srcElement);
      let isHover = this.hasOverLayer(event.srcElement)
      console.log(isHover);
      if (!isHover) {
        this.currentSelectedCard = item
        this.allCardList.splice(index, 1)
        this.selectedCardList.push(item)
        this.selectHistory.push(item)
        this.selectedCardList.sort((a, b)=>{
          return a.picIndex - b.picIndex
        })
        setTimeout(()=>{
          // 判断是否可以消除
          this.checkRemove()
          if (this.allCardList.length == 0) {
            alert('你赢了！')
          }
          if (this.selectedCardList.length >= 7) {
            alert('你输了！')
            this.initData()
          }
        }, 200)
      }
      
    },
    // 判断是否可以消除
    checkRemove() {
      let num = 0
      this.selectedCardList.forEach(item=>{
        if (this.currentSelectedCard.icon == item.icon) {
          num ++
        }
      })
      if (num == 3) {
        this.selectedCardList = this.selectedCardList.filter(item=>{
          return item.icon != this.currentSelectedCard.icon
        })
        this.selectHistory = this.selectHistory.filter(item=>{
          return item.icon != this.currentSelectedCard.icon
        })
      }
    },
    // 监测元素是否被覆盖
    hasOverLayer(element) {
      let document = element.ownerDocument,
      rect = element.getBoundingClientRect(), // 获取目标的矩形信息
      x = rect.x, 
      y = rect.y, 
      width = rect.width, 
      height = rect.height;
      x |= 0;
      y |= 0;
      width |= 0;
      height |= 0;
      // 四顶点取样
      let elements = [
        document.elementFromPoint(x+1, y+1),
        document.elementFromPoint(x + width-1, y+1),
        document.elementFromPoint(x+1, y + height-1),
        document.elementFromPoint(x + width-1, y + height-1)
      ];
      // 判断非本身及非子孙元素
      return elements.filter((el)=> el !== null).some((el)=> el !== element && !element.contains(el));
    },
    // 初始化数据
    initData() {
      this.positionList = []
      this.allCardList = []
      this.selectedCardList = []
      this.currentSelectedCard = {}
      
      let index = 0
      
      // 第一层
      let left = 0
      let top = 0
      for (let i = 0; i < 7; i++) {
        for (let j = 0; j < 7; j++) {
          this.positionList.push({id: index++, picIndex: 1, icon: 'el-icon-platform-eleme', left: left+'px', top: top+'px'})
          left += 50
        }
        left = 0
        top += 50
      }
      
      // 第二层
      left = 25
      top = 25
      for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
          this.positionList.push({id: index++, picIndex: 1, icon: 'el-icon-platform-eleme', left: left+'px', top: top+'px'})
          left += 50
        }
        left = 25
        top += 50
      }
      
      // 生成随机图标
      this.createIcon()
    },
    // 生成随机图标
    createIcon() {
      let index = 0
      this.allCardList = []
      let random = 0
      console.log(random);
      for (let i = 0; i < 303; i++) {
        if (i%3==0) {
          random = Math.floor(Math.random()*11)
        }
        this.allCardList.push({
          id: index++,
          icon: this.iconList[random].icon,
          picIndex: this.iconList[random].picIndex
        })
      }
      this.allCardList.sort(()=>{
        return Math.random() > 0.5 ? 1 : -1
      })
      this.allCardList.forEach((item, index)=>{
        item.id = index
      })
      
      
      // 随机位置
      /* let pos = 0
      this.allCardList.forEach(item=>{
        pos = Math.floor(Math.random()*85)
        item['left'] = this.positionList[pos].left
        item['top'] = this.positionList[pos].top
      }) */
      
      // 循环堆叠
      let pos = 0
      this.allCardList.forEach(item=>{
        item['left'] = this.positionList[pos].left
        item['top'] = this.positionList[pos].top
        pos++
        if (pos > 84) {
          pos = 0
        }
      })
      
      console.log(this.allCardList);
      
    }
    
  }
}
</script>

<style scoped>
  .top-box {
    width: 100%;
    height: 500px;
    background-color: antiquewhite;
  }
  .card-box {
    width: 350px;
    height: 100%;
    background-color: #dddaaa;
    margin: 0 auto;
    position: relative;
  }
  .card {
    width: 48px;
    height: 48px;
    line-height: 48px;
    font-size: 36px;
    border: 1px solid #666;
    text-align: center;
    position: absolute;
    box-shadow: 0px 0px 6px 0px #545454;
    background-color: #fff;
  }
  .selected-card-box {
    width: 350px;
    height: 50px;
    background-color: antiquewhite;
    margin: 0 auto;
  }
  .selected-card {
    width: 48px;
    height: 48px;
    line-height: 48px;
    font-size: 36px;
    border: 1px solid #666;
    text-align: center;
    background-color: #fff;
    display: inline-block;
  }
  .btn {
    margin: 0 auto;
    width: 350px;
    text-align: center;
    margin-top: 24px;
  }
  .el-icon-s-flag {
    color: #aa0000;
  }
  .el-icon-platform-eleme {
    color: #005500;
  }
  .el-icon-delete-solid {
    color: #aa5500;
  }
  .el-icon-s-tools {
    color: #aaaa00;
  }
  .el-icon-user-solid {
    color: #000000;
  }
  .el-icon-warning {
    color: #316394;
  }
  .el-icon-picture {
    color: #00007f;
  }
  .el-icon-upload {
    color: #760000;
  }
  .el-icon-message-solid {
    color: #9a004d;
  }
  .el-icon-video-camera-solid {
    color: #ffaa7f;
  }
  .el-icon-s-platform {
    color: #848441;
  }
  
</style>
