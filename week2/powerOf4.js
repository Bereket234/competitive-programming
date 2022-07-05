/**
 * @param {number} n
 * @return {boolean}
 */
 var isPowerOfFour = function(n) {
    if(n==0){
        return false
    }
    x= Math.round(Math.log(n) / Math.log(4))
    if (Math.pow(4, x) == n)
        return(true)
    else
       return(false)
};