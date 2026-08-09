class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            indexes = [0] * 26
            for char in word:
                indexes[ord(char.lower()) - ord('a')] += 1
            
            if tuple(indexes) in seen:
                seen[tuple(indexes)].append(word)
                continue
                
            seen[tuple(indexes)] = [word]

        return(list(seen.values()))

