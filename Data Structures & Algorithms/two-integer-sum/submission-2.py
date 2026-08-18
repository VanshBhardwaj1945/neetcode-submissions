class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = []

        for i, num in enumerate(nums):
            seen.append(num)
            num2 = target - num
            if num2 in nums:
                return [i, nums.index(num2)]
            
    
        

                    

            


                
