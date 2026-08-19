class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):    
            for j in freq[i]:
                if k <= 0:
                    break

                res.append(j)
                k -= 1
        print(res)
        return res
        

         
            
        

            
        


