//1.1
/*function reverse(str){
    var reversed="";
       for(var i=str.length-1;i>=0;i--){
        reversed+=str[i];
       }
    return reversed
}
str1="hello"
console.log(reverse(str1));
*/
//2
function acronymize(str){
    var expected="";
    if(str[0]!=' '){
        expected+=str[0];
    }
    for(var i=0;i<=str.length;i++){
        if((str[i] ==' ') && (str[i+1]!=' ' )){
           expected+= str[i+1];
        }
    }
    console.log(expected.toUpperCase()) 
}
str1="souha karoui bizerte"
acronymize(str1);


