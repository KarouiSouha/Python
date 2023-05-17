var arr1=[1,2,3];
var separator1=", ";
var expected1="1, 2, 3";
function join(arr1,separator1){
  var str="";

    for(var i=0;i< arr1.length-1;i++){
        str+=arr1[i]+separator1;
    
    }  return str+arr1[arr1.length-1]
}
console.log(join(arr1,separator1))