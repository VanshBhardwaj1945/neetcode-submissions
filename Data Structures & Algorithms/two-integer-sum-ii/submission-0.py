class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            seen[num] = i+1
            temp = target - num

            if temp in seen.keys():
                return list([seen[temp], i+1])
            
