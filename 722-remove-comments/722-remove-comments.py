class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        i, j= 0, 0
        res=[]
        opened= False
        line= []
        
        while i < len(source):
            j=0
            while j< len(source[i]):
                char= source[i][j]
                if len(source[i]) > j+1:
                    next_= source[i][j+1]
                else:
                    next_= None
                
                if not opened and char != '/':
                    line.append(char)
                elif not opened and char == '/':
                    if next_ and next_== '*':
                        opened= True
                        j+=1
                    elif next_ and next_ == '/':
                        break
                    else:
                        line.append(char)
                elif opened and char == '*':
                    if next_== '/':
                        opened =False
                        j+=1
                j+=1
            if not opened and len(line) > 0:
                res.append(''.join(line))
                line= []
            i +=1
        return res