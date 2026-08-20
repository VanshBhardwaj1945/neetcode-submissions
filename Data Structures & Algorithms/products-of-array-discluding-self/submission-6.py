class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inputLen = len(nums)
        prodPre, prodPro = 1, 1
        PrefixList = [0]*(inputLen)
        PostFixList = [0]*(inputLen)
        output = []

        i, j = 0, inputLen-1

        
        for _ in nums:
          PrefixList[i] = prodPre
          prodPre *= nums[i] 
          i += 1

          PostFixList[j] = prodPro
          prodPro *= nums[j] 
          j -= 1

        for pre, pro in zip(PrefixList, PostFixList):
          output.append(pre * pro)

        return output