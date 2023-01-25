class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_apperance= {}
        res= []
        
        for i, c in enumerate(s):
            last_apperance[c]= i
        
        max_= last_apperance[s[0]]
        temp= 0
        for i in range(len(s)):
            
            if i > max_:
                res.append(max_+1- temp)
                temp= max_+1
            max_= max(max_, last_apperance[s[i]])
        res.append(max_ +1 -temp)
        return res