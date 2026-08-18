class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList = {}
        
        for string in strs:
            wordCount = [0] * 26
            
            for char in string:
                wordCount[ord(char.lower()) - ord('a')] += 1
            
            newList.setdefault(tuple(wordCount), []).append(string)

        return (list(newList.values()))


