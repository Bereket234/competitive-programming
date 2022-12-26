# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english= int(input())
if n_english > 0:
    english_np= set(map(int, input().split()))

n_french= int(input())
if n_french > 0:
    french_np= set(map(int, input().split()))

print(len(english_np- french_np))
