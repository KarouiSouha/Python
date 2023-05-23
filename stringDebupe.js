function stringDedupe(str){
    var result=str[0];

    for (var i = 1; i < str.length; i++) {
        if (str[i]!== str[i - 1]) {
          result += str[i];
        }
      }
    
      return result;
    }
  
  console.log(stringDedupe("helloo")); 
