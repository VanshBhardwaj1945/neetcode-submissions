class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordSeen = {}

        for word in strs:
            charSeen = {}

            for char in word:
                charSeen[char] = charSeen.get(char, 0) + 1

            flattened = tuple(sorted(charSeen.items()))
            
            if flattened in wordSeen:
                wordSeen[flattened].append(word)
            else:
                wordSeen[flattened] = [word]
                    
        return list(wordSeen.values())




        return [["dj"]]

        
                    
                


        
            


        