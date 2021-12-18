/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var majorityElement = function(nums) {
    var sorter={}
    var result=[]
    var key
    for(var i= 0; i< nums.length; i++){
        key= nums[i]
        if(sorter[key]){
            sorter[key] +=1
        }else{
            sorter[key]= 1
        }
    }
    for(const property in sorter){
        if(sorter[property] > nums.length/3){
            result.push(property)
        }
    }
    return(result)
};