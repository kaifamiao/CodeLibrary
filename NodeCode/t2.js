console.time('exec')
class blackjack {
    constructor(flower_color) {
        this.flower_color = flower_color
    }
}
var list = [];
for (var i = 1; i <= 13; i++) {
    list.push(new blackjack("黑桃:" + i))
    list.push(new blackjack("红桃:" + i))
    list.push(new blackjack("方块:" + i))
    list.push(new blackjack("梅花:" + i))
}
list.sort(function() {
    return 0.5 - Math.random()
})
console.log('初始化长度:', list.length);
var tmp_list_str = "";
for (var i = 0; i < list.length; i++) {
    tmp_list_str += list[i].flower_color + ','
}
console.log(tmp_list_str);
class player {
    t_list_poker = [];
    t_list_point = [];
    constructor(name, poker, count) {
        this.name = name;
        this.count = count
        this.sum = 0;
        this.isPK = false;
        this.state = 0;
        this.winner ="庄"
    }
    vpointsum() {
        this.sum = 0;
        for (var i = 0; i < this.t_list_point.length; i++) {
            this.sum += this.t_list_point[i]
        }
        return this.sum;
    }
    isPkfunc(vnum) {
        if (vnum == true) this.isPK = true;
    }
}
/*初始化 list是初始化的牌数，playN是多少个玩家+1，初始多少牌*/
function init(list, playN, initSum = 2, ) {
	var iszhuangjia = Math.round(Math.random() * (peopleSum ));
    var playSum = playN + 1
    console.log("开始发牌。。。。", '玩家数量', playSum);
    let play_obj = [];
    for (var i = 0; i < playSum; i++) {
        play_obj[i] = new player("玩家" + i, 0, 0);
    }
    for (var j = 0; j < initSum; j++) {
        for (var i = 0; i < playSum; i++) {
        	//随机产生庄家
            play_obj[i].isPkfunc(i == iszhuangjia);
            var f = list.pop().flower_color
            play_obj[i].t_list_poker.push(f);
            play_obj[i].count = play_obj[i].count + 1;
            play_obj[i].t_list_point.push(parseInt(f.split(':')[1]));
        }
    }
    for (var i = 0; i < playSum; i++) {
        play_obj[i].vpointsum()
    }
    return play_obj;
}
var peopleSum =2;
var play_obj = init(list, peopleSum, 2);
/* 加牌。M是哪个对象、playN是多少玩家*/
function add_poker(M,playN) {
	var playSum = playN + 1
    var f = list.pop().flower_color
    play_obj[M].t_list_poker.push(f);
    play_obj[M].count = play_obj[M].count + 1;
    play_obj[M].t_list_point.push(parseInt(f.split(':')[1]));
    for (var i = 0; i < playSum; i++) {
        play_obj[i].vpointsum()
    }
}
// console.log(play_obj)
/*比较*/
function comparePlay(play_obj){
	var pkOject=new player()
	for(var i=0;i<play_obj.length;i++){
		if(play_obj[i].isPK==true){
			pkOject = play_obj[i];
			console.log("庄家是：",play_obj[i].name);
		}
	}
	//console.log(pkOject)
	for(var i=0;i<play_obj.length;i++){
		if(play_obj[i].sum < 21 && play_obj[i].sum > pkOject.sum && play_obj[i].isPK==false ){
			play_obj[i].winner="赢了";
		}

		if(play_obj[i].sum > 21 && !play_obj[i].isPK && play_obj[i].isPK==false){
			play_obj[i].winner="爆了";
		
		}

		if(play_obj[i].sum <= 21 && play_obj[i].sum <= pkOject.sum && play_obj[i].isPK==false){
			play_obj[i].winner="输了";
		
		}
	}

}
/*加牌*/
add_poker(0,peopleSum)
add_poker(1,peopleSum)
add_poker(0,peopleSum)


comparePlay(play_obj)
console.log(play_obj);

//console.log(play_obj);
// var tmp=new player()
// for(var i=0;i<play_obj.length;i++){
	
// 	tmp=play_obj[0];
// 	if( tmp.sum < play_obj[i].sum ){
// 		tmp=play_obj[i+1];
// 	}

// }
//console.log(tmp);
console.log("");
console.log("=====================================================================剩余牌数=====================================================================");
console.log("");
tmp_list_str = "";
for (var i = 0; i < list.length; i++) {
    tmp_list_str += list[i].flower_color + ','
}
console.log(tmp_list_str);
console.log('剩余牌数：', list.length);
console.timeEnd('exec')
