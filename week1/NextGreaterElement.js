/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var nextGreaterElement = function(nums1, nums2) {
    var stack=[]
    var result= []
    var lib= {}
    for(var i=0; i<nums2.length;i++){
        if(stack.length>0){
            for(j=(stack.length);j>=0;j--){
               if(stack[j-1] < nums2[i]){
                    lib[stack[j-1]]= nums2[i]
                    stack.pop()
                }else{
                    stack.push(nums2[i])
                    break
                } 
            }
        }else{
            stack.push(nums2[i])
        }
    }
    for(var i=0; i<stack.length; i++){
        lib[stack[i]]=-1
    }
    for (var i=0; i<nums1.length; i++){
        result.push(lib[nums1[i]])
    }
    return(result)
};