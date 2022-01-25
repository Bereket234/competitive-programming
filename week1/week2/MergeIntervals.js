/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
    var stack=[]
    intervals=intervals.sort((x,y)=> x[0]- y[0])
    for(var i=0; i <intervals.length; i++){
        if(stack.length==0){
            stack.push(intervals[i])
        }else if(stack[stack.length-1][1]>= intervals[i][0]){
            stack[stack.length-1][1]= Math.max(intervals[i][1], stack[stack.length-1][1])
        }else{
            stack.push(intervals[i])
        }
    }
    return(stack)
};