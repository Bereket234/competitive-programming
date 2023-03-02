class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for c in s:
            if stack and ((c == ')' and stack[-1] == "(") or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{')):
                stack.pop()
                continue
            stack.append(c)
            
        return len(stack) == 0