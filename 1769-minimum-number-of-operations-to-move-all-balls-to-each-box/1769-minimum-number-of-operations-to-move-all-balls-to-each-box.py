class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res= [0] *len(boxes)
        balls= 0
        ops= 0
        
        #block of code that iterates through the nums and find the acimum operation
        
        for box in boxes:
            ops+= balls
            if box=="1":
                balls +=1
        balls_right= 0
        ops_right= 0
        for i in range(len(boxes)-1, -1, -1):
            res[i]= ops + ops_right
            if boxes[i] == "1":
                balls-= 1
                balls_right +=1
            ops-=balls
            ops_right += balls_right
        return res
                