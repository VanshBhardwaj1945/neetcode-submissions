class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordSeen = {}

        for word in strs:
            CharSeen = {}
            for char in word:
                CharSeen[char] = CharSeen.get(char, 0) + 1
    
            key = tuple(sorted(CharSeen.items()))

            if key not in wordSeen:
                wordSeen[key] = []

            wordSeen[key].append(word)
        
        output = list(wordSeen.values())

        return output

            
        
                    
                


        
            


        