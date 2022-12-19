/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    
};/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    var stack= []
    var m, k
    var n= temperatures.length
    var result= new Array(n).fill(0)
    
    for (var i=0; i<temperatures.length; i++){
        if (stack.length>0){
            k=stack.length
            
            for(var j=k; j>=0; j--){
                m=stack.length-1
                if(temperatures[stack[m]] < temperatures[i]){
                    result[stack[m]]= i-stack[m]
                    stack.pop()
                }else{
                    stack.push(i)
                    break
                }
            }
        }else{
            stack.push(i)
        }
    }
    return(result)
};