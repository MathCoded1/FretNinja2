first =  10
second = 3
third =  8
fourth = 1
fifth =  5
sixth =  10

var zero
var one 
var two 
var three
var four
var five
var six
var seven
var eight
var nine
var ten
var eleven

var fretNums ="     0        1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16       17       18       19       20       21"
var fretLines="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
function fillstr(root){
var a = fillarr(root)
return "||   "+a[0]+"  ||   "+a[1]+"  ||   "+a[2]+"  ||   "+a[3]+"  ||   "+a[5]+"  ||   "+a[6]+"  ||   "+a[7]+"  ||   "+a[8]+"  ||   "+a[9]+"  ||   "+a[10]+"  ||   "+a[11]+"  ||   "+a[0]+"  ||   "+a[1]+"  ||   "+a[2]+"  ||   "+a[3]+"  ||   "+a[4]+"  ||   "+a[5]+"  ||   "+a[6]+"  ||   "+a[7]+"  ||   "+a[8]+"  ||   "+a[9]+"  ||   "+a[10]+"  ||"

};
console.log(fretNums)
console.log(fretLines)
console.log(fillstr(sixth))
console.log(fillstr(fifth))
console.log(fillstr(fourth))
console.log(fillstr(third))
console.log(fillstr(second))
console.log(fillstr(first))
console.log(fretLines)
console.log(fretNums)







function change(position){
switch(position){
case 1:
return "G " 
case 2:
return "G#"
case 3:
return "A "
case 4:
return "A#"
case 5:
return "B "
case 6:
return "C "
case 7:
return "C#"
case 8:
return "D "
case 9:
return "D#"
case 10:
return "E "
case 11:
return "F "
case 12:
return "F#"
}
};

function fillarr(zeroth){
var a = new Array(12)
a[0] = change(zeroth)
a[1] = change(add(zeroth,1))
a[2] = change(add(zeroth,2))
a[3] = change(add(zeroth,3))
a[4] = change(add(zeroth,4))
a[5] = change(add(zeroth,5))
a[6] = change(add(zeroth,6))
a[7] = change(add(zeroth,7))
a[8] = change(add(zeroth,8))
a[9] = change(add(zeroth,9))
a[10] = change(add(zeroth,10))
a[11] = change(add(zeroth,11))
return a
};

function add(num1, num2){
if (num1 +num2 <=12){
return num1 +num2}
else{
return num1 + num2 - 11;
}
};
