class Solution:
    def average(self, salary: List[int]) -> float:
        res=0
        min_= min(salary[0], salary[1])
        max_= max(salary[0], salary[1])
        
        for i in range(2, len(salary)):
            if salary[i] < min_:
                res+=min_
                min_= salary[i]
            elif salary[i] > max_:
                res+= max_
                max_= salary[i]
            else:
                res+= salary[i]
        return res/(len(salary)-2)