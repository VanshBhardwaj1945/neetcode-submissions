class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [0] * n, [0] * n
        prodLeft, prodRight = 1, 1
        i, j = 0, n - 1

        while i < n:
            left[i] = prodLeft
            prodLeft *= nums[i]
            i += 1

            right[j] = prodRight
            prodRight *= nums[j]
            j -= 1
        
        

        res = []
        for k in range(n):
            product = left[k] * right[k]
            res.append(product)
        
        return(res)