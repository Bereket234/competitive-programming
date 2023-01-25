class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        first_num= num1.split('+')
        second_num= num2.split('+')
        first_num= [int(first_num[0]), int(first_num[1][:len(first_num[1])-1])]
        second_num= [int(second_num[0]), int(second_num[1][:len(second_num[1])-1])]
        real= (first_num[0] * second_num[0]) - (first_num[1] * second_num[1])
        imaginary= (first_num[0] * second_num[1]) + (first_num[1] * second_num[0])
        res=[str(real) , str(imaginary) +'i']
        return '+'.join(res)