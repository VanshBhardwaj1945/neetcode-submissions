class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        buckets = [[] for i in range(len(nums) + 1)]
        seen = {}
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for key, value in seen.items():
            buckets[value].append(key)

        output = []
        for index in range(len(buckets)-1, -1, -1):
            for num in buckets[index]:
                if k > 0:
                    output.append(int(num))
                    k -= 1
                else:
                    break

        return output
        
           