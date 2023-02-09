class Solution:
    def compress(self, chars: List[str]) -> int:
        i= 0
        
        holder= 0
        cnt= 0
        s_cnt= ''
        
        for seeker in range(len(chars)):
            h, s= chars[holder], chars[seeker]
            
            
            if h != s:
                print(h,s,i)
                s_cnt= '' if cnt == 0 else str(cnt+1)
                chars[i] = h
                i+=1
                holder= seeker
                for n in s_cnt:
                    chars[i] = n
                    i+=1
            cnt= seeker - holder
        
        
        chars[i] = chars[holder]
        s_cnt= '' if cnt == 0 else str(cnt+1)
        i+=1
        holder= seeker
        for n in s_cnt:
            chars[i] = n
            i+=1

        return i
        

                