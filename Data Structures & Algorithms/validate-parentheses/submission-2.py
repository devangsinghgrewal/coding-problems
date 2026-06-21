class Solution:
    def isValid(self, s: str) -> bool:
        pr = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        # l = 0
        # r = len(s)-1
        # while l<=r:
        #     if pr[s[l]]!=s[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        open_brackets = []
        for i in range(len(s)):
            if s[i] in pr.keys():
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


            
            
        