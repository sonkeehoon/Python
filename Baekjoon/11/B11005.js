const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split(' '); // 윈도우에서는 ./input.txt
// let input = fs.readFileSync("/dev/stdin").toString().split(' '); 백준에 제출할때(linux에서)만 /dev/stdin 으로
N = Number(input[0]);
B = Number(input[1]);
var arr = [];
var res = '';
while (N!=0) {
    arr.push(N%B);
    N = parseInt(N / B);
}
arr.reverse();
for (var i = 0; i<arr.length; i++){
    tmp = arr[i];
    if (tmp >= 10){
        res += String.fromCharCode(tmp+55);
        continue;
    }
    res += arr[i];

}
console.log(res);

