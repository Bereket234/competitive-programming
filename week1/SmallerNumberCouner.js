/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    var counter=0
    var counterArray= []
    
    for(var i=0; i<nums.length;i++){
        for(var j=0;j<nums.length; j++){
            if (nums[i]> nums[j]){
                counter +=1
            }
        }
        counterArray[i]=counter
        counter=0
    }
    return(counterArray)
};
