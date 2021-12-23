/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    var counter=0
    var result={}
    var x
    for(var i=0; i<nums.length; i++){
        if(!(nums[i]+'' in result || k-nums[i]+'' in result)){
            result[nums[i]]= 1
        }else if(result[k-nums[i]+''] > 0) { 
            result[k-nums[i]]-= 1
            counter++
        }else if(result[k-nums[i]] == 0){
            delete result[k-nums[i]]
            result[nums[i]]=1
        }else{
            result[nums[i]]++
        }
    }
    return(counter)
};