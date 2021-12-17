/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    var result=false
    var stack=[]
    for(var i=0; i<s.length; i++){
        if ( s[i]=='['|| s[i]=='('|| s[i]=='{' ){
            stack.push(s[i])
        }else{
            if(stack[stack.length-1]=='(' && s[i]==')'){
                result=true
                stack.pop()
            }else if(stack[stack.length-1]=='{' && s[i]=='}'){
                result=true
                stack.pop()
            }else if(stack[stack.length-1]=='[' && s[i]==']'){
                result=true
                stack.pop()
            }else{
                result=false
                break
            }
        }
    }
    if(stack.length>0){
        result=false
    }
    return(result)
};