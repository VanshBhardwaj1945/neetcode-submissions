class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0                  # Starts at the beginning
        j = len(s) - 1     # Starts at the very end

        while i < j:
            
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            
            #print('i - ' + s[i].lower() + ' j - ' + s[j].lower())
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


            