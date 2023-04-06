class Solution:
    def check_collision(self, arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] & arr2[i]:
                return False
        return True
    
    def maxProduct(self, words: List[str]) -> int:
        cnt= [[0] * 26 for i in range(len(words))] 
        res= 0
        
        for i, word in enumerate(words):
            for ch in word:
                cnt[i][ord(ch) - 97]= 1
        
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.check_collision(cnt[i], cnt[j]):
                    res= max(res, len(words[i]) * len(words[j]))
        return res
                