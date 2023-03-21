class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res= []
        
        def backtrack(start, arr):
            if arr and int(arr[-1]) > 255:
                return 
            if arr and len(arr[-1]) > 1 and arr[-1][0] == '0':
                return 
            
            if len(arr) == 4:
                if start== len(s):
                    res.append('.'.join(arr))
                return
            
            for i in range(start, min(start + 3, len(s))):
                arr.append(s[start: i+1])
                backtrack(i+1, arr)
                arr.pop()
            
        backtrack(0, [])
        return res