class Node:
    def __init__(self, val= 0, left= None, right= None):
        self.val=val
        self.left= left
        self.right= right
class BinaryTree:
    def __init__(self) -> None:
        self.root= None
    def look_up(self, val:int) -> bool:
        if not self.root:
            return False
        curr= self.root
        while curr:
            if curr.val== val:
                return True
            if curr.val < val:
                curr= curr.left
            else:
                curr= curr.right
        return False
    def remove(self, val:int)-> bool:
        if not self.root:
            return False
        curr= self.root
        parentNode= None
        while curr:
            if curr.val== val:
                if curr.right:
                    temp= curr.right
                    tempParent= None
                    while temp.left:
                        tempParent= temp
                        temp= temp.left
                    temp.left= curr.left
                    temp.rigth= curr.right
                    if tempParent:
                        tempParent.left= temp.left
                    if parentNode.val > curr.val:
                        parentNode.left= temp
                    else:
                        parentNode.right= temp
                else:
                    if parentNode.val > curr.val:
                        parentNode.left= curr.left
                    else:
                        parentNode.right= curr.left
            if curr.val > val:
                parentNode= curr
                curr= curr.left
            else:
                parentNode= curr
                curr= curr.right

    def insert(self, val:int) -> bool:
        newNode= Node(val)
        temp= self.root
        if not temp:
            temp= newNode
            return self
        
        else:
            if temp.val == val:
                return False
            if temp.val > val:
                while 1:
                    if not temp.left:
                        temp.left= newNode
                        return True
                    temp= temp.left
            if temp.val < val:
                while 1:
                    if not temp.right:
                        temp.right= newNode
                        return True
                    temp= temp.right

tree= BinaryTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(5)
tree.remove(6)


print()
