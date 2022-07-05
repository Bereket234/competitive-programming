/**
 * @param {number} n
 * @return {boolean}
 */
 var isPowerOfThree = function(n) {
    if(n==0){
        return false
    }
    x= Math.round(Math.log(n) / Math.log(3))
    console.log(x)
    console.log(Math.pow(3, x))
    if (Math.pow(3, x) == n)
        return(true)
    else
       return(false)
};