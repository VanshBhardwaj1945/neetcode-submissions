class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        buckets = [[] for i in range(len(nums) + 1)]
        seen = {}
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for key, value in seen.items():
            buckets[value].append(key)
        
        output = []
        for i in range(len(buckets)-1, -1, -1):
            for j in buckets[i]:
                if k <= 0:
                    break
                
                output.append(j)
                k -= 1

        return output
        

            
        


