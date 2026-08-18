class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.length() == t.length():
            for char in s:
                if char not in t:
                    return False
            return True
        else:
            return False
                    
