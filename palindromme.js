function palindrome(str){
    
    for(var i=0;i<=Math.ceil(str.length/2);i++){
    if(str[i]!=str[str.length-i-1]){
        return false
    }
}
return true
}
var result = palindrome("radar");
console.log(result);




function decodeStr(str){
    
}