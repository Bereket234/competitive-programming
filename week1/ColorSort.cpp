/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    var colorsCount=[]
    var result=[]
    for(var i=0; i< 3; i++){
        colorsCount[i]=0
    }
    
    for(var i=0;i<nums.length; i++){
        colorsCount[nums[i]]++
    }
    for(var i=0,k=0;i<3;i++){
        for (var j=0; j< colorsCount[i]; j++){
            nums[k]=i
            k++
        }
    }
};
