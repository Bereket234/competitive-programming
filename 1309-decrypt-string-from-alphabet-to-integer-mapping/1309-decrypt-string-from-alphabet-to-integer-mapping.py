class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp= {}
        res=''
        cnt=0
        num=''
        for i in range(97, 97+26):
            mp[i-96]= chr(i)
        for i in range(len(s)-1, -1, -1):
            if cnt>0:
                num= s[i] + num
                cnt-=1
                if cnt==0:
                    res= mp[int(num)] + res
            elif s[i] == '#':
                cnt =2
                num= ''
                
            else:
                res = mp[int(s[i])] + res
        return res