class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        output = []
    
        for i in range(len(nums)):
            seen.append(nums[i])

            for j in range(len(seen)):
                if seen[j] != nums[i]:
                    if seen[j] + nums[i] == target:
                        return [j, i]
                    

                    

            


                
