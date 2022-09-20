/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    var x=0
    var temp=0
  if(n==0){
      return 0
  }else if (n==1){
      return 1
  }
     return(fib(n-1)+fib(n-2))
};