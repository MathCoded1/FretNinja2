
var tuning = ["E", "A", "D", "G", "B", "E"];
var fretNums = "     0    "
for( var i = 1; i < 11; i ++){
    fretNums +="    "+i+"    ";
}
for( var i = 11; i < 22; i ++){
    fretNums +="   "+i+"    ";
}
var fretLines="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------";
function fillstr(rootNote){
var a = fillarr(rootNote);
var str = "||   ";
for( i = 0; i < 12; i++){
str += a[i]+"  ||   ";
}
for ( i = 0; i < 10; i++){
    str += a[i]+"  ||   ";
}
return str;
}

console.log(fretNums);
console.log(fretLines);
var tuningMod=tuning.reverse();
for( j = 0; j < 6; j++){
    console.log(fillstr(change(tuningMod[j])));
}
console.log(fretLines);
console.log(fretNums);


function change(note){
    switch(note){
    case "G":
    return 1;
    case "G#":
    return 2;
    case "A":
    return 3;
    case "A#":
    return 4;
    case "B":
    return 5;
    case "C":
    return 6;
    case "C#":
    return 7;
    case "D":
    return 8;
    case "D#":
    return 9;
    case "E":
    return 10;
    case "F":
    return 11;
    case "F#":
    return 12;
    }
    }




function changeBack(position){
switch(position){
case 1:
return "G "; 
case 2:
return "G#";
case 3:
return "A ";
case 4:
return "A#";
case 5:
return "B ";
case 6:
return "C ";
case 7:
return "C#";
case 8:
return "D ";
case 9:
return "D#";
case 10:
return "E ";
case 11:
return "F ";
case 12:
return "F#";
}
}

function fillarr(zeroth){
var a = new Array(12);
a[0] = changeBack(zeroth);
a[1] = changeBack(add(zeroth,1));
a[2] = changeBack(add(zeroth,2));
a[3] = changeBack(add(zeroth,3));
a[4] = changeBack(add(zeroth,4));
a[5] = changeBack(add(zeroth,5));
a[6] = changeBack(add(zeroth,6));
a[7] = changeBack(add(zeroth,7));
a[8] = changeBack(add(zeroth,8));
a[9] = changeBack(add(zeroth,9));
a[10] = changeBack(add(zeroth,10));
a[11] = changeBack(add(zeroth,11));
return a;
}

function add(num1, num2){
if (num1 + num2 <=12){
return num1 + num2;}
else{
return num1 + num2 - 11;
}
}
