if __name__ == '__main__':
    N = int(input())
    res=[]
   
    def make_ops(arr,ops):
        if ops[0] == 'insert':
            arr.insert(int(ops[1]), int(ops[2]))
            return arr
        elif ops[0] == 'print':
            print(arr)
            return arr
        elif ops[0] == 'remove':
            arr.remove(int(ops[1]))
            return arr
        elif ops[0] == 'append':
            arr.append(int(ops[1]))
            return arr
        elif ops[0]== 'sort':
            arr.sort()
            return arr
        elif ops[0] == 'pop':
            arr.pop()
            return arr
        elif ops[0] == 'reverse':
            arr.reverse()
            return arr
        
    for i in range(N):
        ops= list(input().split())
        res= make_ops(res,ops)
        
            