class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            min_= i
            for j in range(i, len(names)):
                if heights[j] > heights[min_]:
                    min_= j
            heights[min_], heights[i]= heights[i], heights[min_]
            names[min_], names[i]= names[i], names[min_]
        return names