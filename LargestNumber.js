/**
 * @param {number[]} nums
 * @return {string}
 */
 var largestNumber = function(nums) {
    var min, temp
    for(var i=0; i<nums.length; i++){
        nums[i]= nums[i].toString()
    }
    for(var i=0; i<nums.length; i++){
        for(var j=0; j<nums.length; j++){
            if(Number(nums[j]+nums[j+1])< Number(nums[j+1]+nums[j])){
                temp= nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
            }
        }
    }
    if (nums[0]==0){
        return("0")
    }
    return(nums.join(''))
};