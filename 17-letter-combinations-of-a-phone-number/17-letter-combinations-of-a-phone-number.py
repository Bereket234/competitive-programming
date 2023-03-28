class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c= 97
        res= []
        dic= defaultdict(list)
        for i in range(2, 7):
            for j in range(3):
                dic[str(i)].append(chr(c)) 
                c+=1
        for i in range(4):
            dic['7'].append(chr(c))
            c+=1
        for i in range(3):
            dic['8'].append(chr(c))
            c+=1
        for i in range(4):
            dic['9'].append(chr(c))
            c+=1
        def backtrack(i, arr):
            if i == len(digits):
                if len(arr) != 0:
                    res.append(''.join(arr))
                return
            for j in range(len(dic[digits[i]])):
                arr.append(dic[digits[i]][j])
                backtrack(i + 1, arr)
                arr.pop()
        
        backtrack(0, [])
        return res