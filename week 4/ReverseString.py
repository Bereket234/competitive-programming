class Solution:
    def reverseParentheses(self, s: str) -> str:
        string= list(s)
        stack=[]
        
        for i in range(len(string)):
            if string[i] == '(':
                stack.append(i)
            elif string[i] == ')':
                string= string[0:stack[-1]] + list(reversed((string[stack[-1]: i+1]))) + string[i+1:]
                stack.pop()
        
        return(''.join([i for i in string if i not in '()']))
        