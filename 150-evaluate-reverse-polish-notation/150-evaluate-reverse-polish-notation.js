/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    var stack=[]
    var x=0
    if (tokens.length<2){
        return tokens[0]
    }else{
        for(var i=0; i< tokens.length; i++){
         if (tokens[i]=='+' || tokens[i]=='-' || tokens[i]=='*' || tokens[i]=='/'){
           x= Math.trunc(eval('(' +stack[stack.length-2] + ')' + ''  +tokens[i] + ''+ '('+stack[stack.length-1]+')' ))
           stack.pop()
            stack.pop()
            stack.push(x)
        }else{
            stack.push(tokens[i])
        }
    }
    }
    
    return (x)
};