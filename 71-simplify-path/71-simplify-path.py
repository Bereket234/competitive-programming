class Solution:
    def simplifyPath(self, path: str) -> str:
        path= path.split('/')
        stack=[]
        
        for dic in path:
            if dic == '..':
                if stack:
                    stack.pop()
                continue
            elif dic == '' or dic == '.':
                continue
            stack.append(dic)
        return '/' + '/'.join(stack)