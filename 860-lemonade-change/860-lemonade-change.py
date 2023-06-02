class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt= {10: 0, 5: 0, 20: 0}
        
        for bill in bills:
            if bill == 20:
                if cnt[10] and cnt[5]:
                    cnt[10]-=1
                    cnt[5]-= 1
                elif cnt[5] >= 3:
                    cnt[5]-=3
                else:
                    return False
            if bill == 10:
                if cnt[5]:
                    cnt[5]-=1
                else:
                    return False
            cnt[bill] +=1
        return True