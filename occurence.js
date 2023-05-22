function occurence(arr){
    var obj={};
    for(c of arr){
        if(obj.hasOwnProperty(c)){
             obj[c]+=1;
        }
        else{
           obj[c]=1;
        }
    }
    return obj
}
console.log(occurence(["a","a","a","bob","b","b"]))
