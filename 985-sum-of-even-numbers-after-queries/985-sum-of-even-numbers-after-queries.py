class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_= 0
        res= []
        #this block calculates the sum of even numbers
        for num in nums:
            if num%2 ==0:
                sum_+=num
        """block that finds for even numbers and id it is even it adds the val only if it is odd it adds the           sum of val and number at index"""
        for query in queries:
            index, val= query[1], query[0]
            num= nums[index]
            if num % 2 == 0:
                if (num + val)%2 == 0:
                    sum_ += val
                    nums[index]= val+ num
                else:
                    sum_-= num
                    nums[index]= val + num
            else:
                if (num + val) % 2 ==0:
                    sum_+= val + num
                    nums[index]= num +val
                else:
                    nums[index]= num +val
            
            res.append(sum_)
                
                
                    
        return res
        
        