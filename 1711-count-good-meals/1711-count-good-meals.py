class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pows= set()
        res=0
        visited={}
        MOD= 10**9 + 7
        for i in range(22):
            pows.add(2**i)
        for num in deliciousness:
            for i in pows:
                if i - num in visited:
                    res+= visited[i-num]
            visited[num]= 1+ visited.get(num, 0)
        return res % MOD