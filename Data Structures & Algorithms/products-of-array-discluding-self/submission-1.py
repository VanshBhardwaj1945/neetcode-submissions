class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)

        prod = 1
        for num in nums:
            if num != 0:
                prod *= num

        for num in nums:
            if zero_count == 1:
                temp = prod if num == 0 else 0
            else:
                temp = prod // num
            res.append(temp)

        
        return res