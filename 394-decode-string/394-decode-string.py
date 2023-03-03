class Solution:
    def decodeString(self, s: str) -> str:
        num_stack= []
        char_stack= []
        curr= []
        i= 0
        
        while i < len(s):
            c= s[i]
            if c == '[':
                i+=1
                if not s[i].isdigit():
                    char_stack.append(s[i])
                    i+=1
                else:
                    char_stack.append('')
            elif c == ']':
                curr= char_stack.pop()
                curr= num_stack.pop() * curr
                if char_stack:
                    char_stack.append(char_stack.pop()+curr)
                else:
                    char_stack.append(curr)
                i+=1
            elif c.isdigit():
                curr=[]
                while i < len(s) and s[i].isdigit():
                    curr.append(s[i])
                    i+=1
                num_stack.append(int(''.join(curr)))
            else:
                if char_stack:
                    curr= char_stack.pop() + c
                    char_stack.append(curr)
                    i+=1
                else:
                    char_stack.append(c)
                    i+=1
                    
        
        return ''.join(char_stack)