/**
 * @param {number[]} nums
 * @return {number}
 */
 var minPairSum = function(nums) {
    var result=0
    n=nums.length
    nums.sort((x,y)=> x-y)
    for(var i=0; i<n/2; i++){
        if((nums[i]+ nums[n-1-i ]) > result){
            result=nums[i]+ nums[n-1-i ]
        }
    }
    return(result)
};