class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return ['0']
            
            prev_s= helper(n-1)
            curr_s= [i for i in prev_s]
            curr_s.append('1')
            for i, c in enumerate(prev_s):
                if c == '1':
                    prev_s[i]= '0'
                else:
                    prev_s[i]= '1'
                    
            prev_s.reverse()      
            curr_s= curr_s + prev_s
            return curr_s
        return helper(n)[k-1]