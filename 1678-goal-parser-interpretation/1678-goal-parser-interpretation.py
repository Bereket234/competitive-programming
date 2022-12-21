class Solution:
    def interpret(self, command: str) -> str:
        res= []
        
        for char in command:
            if char == 'G':
                res.append('G')
            elif char == '(':
                res.append('o')
            elif char== 'a':
                res.pop()
                res.append('al')
        return ''.join(res)