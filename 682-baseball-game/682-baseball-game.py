class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack= []
        
        for ops in operations:
            if ops =='C':
                stack.pop()
                continue
                
            elif ops == 'D':
                ops= stack[-1] * 2
                
            elif ops == '+':
                ops= stack[-1] + stack[-2]
                
            stack.append(int(ops))
            
        return sum(stack)
            