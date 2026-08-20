class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            temp = target - num

            if temp in seen:
                return [seen[temp], i+1]

            seen[num] = i+1