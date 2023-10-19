class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        mod= 10 ** 9 + 7
        curr= [1] * 10
        prev= curr.copy()
        graph= {
            0: [6, 4],
            1: [6, 8],
            2: [7, 9],
            3: [8, 4],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [3, 1],
            9: [2, 4]
        }
        
        for _ in range(n-1):
            prev= curr.copy()
            for j in range(10):
                curr[j] = 0
            for i in range(len(curr)):
                for element in graph[i]:
                    curr[element] += prev[i]
        return sum(curr) % mod
            
        