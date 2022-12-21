class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1= num1 + '*' +num2
        return str(eval(num1))
        