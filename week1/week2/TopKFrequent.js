var topKFrequent = function(nums, k) {
    var sorter= {}
    var result= []
    var key,max=-1
    for(var i=0; i<nums.length; i++){
        key= nums[i]
        if(sorter[key]){
            sorter[key] +=1
        }else{
            sorter[key]= 1
        }
    }
    var sorted=[]
    for(var i in sorter){
        sorted.push([i, sorter[i]])
    }
    sorted.sort((x, y)=> x[1] -y[1])
    console.log(sorted)
    for(var i=(sorted.length-1); i>= (sorted.length-k); i--){
        result.push(Number(sorted[i][0]))
    }
    return(result)
};
console.log(topKFrequent([1,1,1,2,2,3], 2))