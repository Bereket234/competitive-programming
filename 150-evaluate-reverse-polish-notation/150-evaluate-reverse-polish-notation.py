class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        ops= {"+", "-", "/", "*"}
        
        for token in tokens:
            val = token
            if token in ops:
                val1= stack.pop()
                val2= stack.pop()
                val= int(eval("".join([val2, token, val1])))
            stack.append(str(val))
            
        return int(stack[0])