# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_power_mode(a, b, m):
    print(pow(a, b))
    print(pow(a, b, m))


if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())

    calculate_power_mode(a, b, m)
