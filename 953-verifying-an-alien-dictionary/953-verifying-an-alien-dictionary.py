class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict={}
        max_s= len(max(words, key= lambda s:len(s)))
        for i in range(len(order)):
            order_dict[order[i]]= i
        
        for i in range(len(words)-1):
            w1, w2= words[i], words[i+1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_dict[w1[j]] > order_dict[w2[j]]:
                        return False
                    break
        return True
                    
        