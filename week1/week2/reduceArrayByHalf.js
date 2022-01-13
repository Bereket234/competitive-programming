/**
 * @param {number[]} arr
 * @return {number}
 */
 var minSetSize = function(arr) {
    var counter={}
    var result=1
    for(var i=0; i<arr.length; i++){
        if(!(arr[i]+'' in counter)){
            counter[arr[i]]= 1
        }else{
            counter[arr[i]]++
        }
    }
      var sorted=[]
      for(var i in counter){
          sorted.push([i, counter[i]])
      }
      sorted.sort((x, y)=> x[1] -y[1])
      sorted= sorted.reverse()
      console.log(sorted)
      var sum= sorted[0][1]
      for(var i=1; i<sorted.length; i++){
          if(sum < arr.length/2){
              sum+= sorted[i][1]
              result++
          }else{
              break
          }
      }
      return(result)
  };