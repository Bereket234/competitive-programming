# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
testCase= {}
for i in range(n):
    s= input()
    testCase[s]= 1+ testCase.get(s, 0)

print(len(testCase))
for i,v in testCase.items():
    print(v, end=' ')
    
