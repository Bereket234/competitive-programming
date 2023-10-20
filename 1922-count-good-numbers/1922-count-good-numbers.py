class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod= 10**9 + 7
        res= pow(20, n//2, mod)
        if n % 2 == 0:
            return (res)
        return (res * 5)% mod