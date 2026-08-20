class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS, seenT = {}, {}

        if len(s) != len(t):
            return False
        
        for i, j in zip(s, t):
            seenS[i] = seenS.get(i, 0) + 1
            seenT[j] = seenT.get(j, 0) + 1
        
        if seenS != seenT:
            return False

        return True