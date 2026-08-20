class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            product = 1
            left, right = 0, len(nums)-1
            while left < i:
                product *= nums[left]
                left += 1
            while right > i:
                product *= nums[right]
                right -= 1      
            
            res.append(int(product))

        
        return res