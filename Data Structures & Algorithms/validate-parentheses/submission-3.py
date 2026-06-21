class Solution:
    def isValid(self, s: str) -> bool:
        pr = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        open_brackets = []
        for i in range(len(s)):
            if s[i] in pr:
                open_brackets.append(s[i])
            else:
                if open_brackets and pr[open_brackets[-1]]== s[i]:
                    open_brackets.pop()
                else:
                    return False
        
        if not open_brackets:
            return True
        else:
            return False

#O(N) Time
#O(N) space due to open_brackets worst case


            
            
        