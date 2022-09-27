console.time('test')
var creatSum = function() {
    var N = 52;
    var arr1 = [];

    function randomNum() { //生成随机数
        var num = Math.round(Math.random() * (N - 1));
        if (arr1.indexOf(num) == -1) { //去重
            arr1.push(num);
        }
        if (arr1.length < N) {
            randomNum();
        }
    }
    randomNum();

    creatSum=arr1;
    return arr1;
}

//console.log(creatSum());
//console.log('array length is :',creatSum.length);
/*冒泡排序*/
// function dub_sort(arr) {
//     var a = arr;
//     for (i = 0; i < a.length; i++) {
//         for (j = i; j < a.length; j++) {
//             var b;
//             if (a[i] > a[j]) {
//                 b = a[j];
//                 a[j] = a[i]
//                 a[i] = b
//             }
//         }
//     }
//     console.log(a)
// }



class blackjack{

    constructor(create_sum){
        if(create_sum>=0 && create_sum<=12){
            this.flower_color="黑桃"
            this.create_sum=create_sum+1

        }
        if(create_sum>=13 && create_sum<=25){
            this.flower_color="红桃"
            this.create_sum=create_sum-13+1
        }
        if(create_sum>=26 && create_sum<=38){
            this.flower_color="方片"
            this.create_sum=create_sum-26+1
        }
        if(create_sum>=39 && create_sum<=51){
            this.flower_color="梅花"
            this.create_sum=create_sum-39+1
        }
        
   
    }
}

// dub_sort(creatSum);
creatSum()
var list=[];
for(var i=0;i<creatSum.length;i++){
    list.push(new blackjack(creatSum[i]))
    console.log(list[i]);
}

// for(var i=0;i<list.length;i++){
//     console.log(list[i]);
// }
console.log("list length is" ,list.length);
// 
console.log(list.pop(),list.pop(),list.pop(),list.pop());





console.log("list last length is" ,list.length);

console.timeEnd('test')
console.log('\x1B[31m%s\x1B[0m', '这是红色')
console.log('\x1B[31m这是红色\x1B[0m')
///const colors = require('colors-console')

//console.log('\x1B[36m%s\x1B[0m', info);  //cyan  
//console.log('\x1B[33m%s\x1b[0m:', path);  //yellow  
var styles = {  
    'bold'          : ['\x1B[1m',  '\x1B[22m'],  
    'italic'        : ['\x1B[3m',  '\x1B[23m'],  
    'underline'     : ['\x1B[4m',  '\x1B[24m'],  
    'inverse'       : ['\x1B[7m',  '\x1B[27m'],  
    'strikethrough' : ['\x1B[9m',  '\x1B[29m'],  
    'white'         : ['\x1B[37m', '\x1B[39m'],  
    'grey'          : ['\x1B[90m', '\x1B[39m'],  
   'black'         : ['\x1B[30m', '\x1B[39m'],  
    'blue'          : ['\x1B[34m', '\x1B[39m'],  
    'cyan'          : ['\x1B[36m', '\x1B[39m'],  
    'green'         : ['\x1B[32m', '\x1B[39m'],  
    'magenta'       : ['\x1B[35m', '\x1B[39m'],  
    'red'           : ['\x1B[31m', '\x1B[39m'],  
    'yellow'        : ['\x1B[33m', '\x1B[39m'],  
    'whiteBG'       : ['\x1B[47m', '\x1B[49m'],  
    'greyBG'        : ['\x1B[49;5;8m', '\x1B[49m'],  
    'blackBG'       : ['\x1B[40m', '\x1B[49m'],  
    'blueBG'        : ['\x1B[44m', '\x1B[49m'],  
    'cyanBG'        : ['\x1B[46m', '\x1B[49m'],  
    'greenBG'       : ['\x1B[42m', '\x1B[49m'],  
    'magentaBG'     : ['\x1B[45m', '\x1B[49m'],  
    'redBG'         : ['\x1B[41m', '\x1B[49m'],  
    'yellowBG'      : ['\x1B[43m', '\x1B[49m']  
};  
console.log('\x1B[33m%s\x1b[0m:', "path");  //yellow  