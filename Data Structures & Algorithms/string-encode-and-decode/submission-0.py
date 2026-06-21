class Solution:

    def encode(self, strs):
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result

    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])        # read the length
            result.append(s[j+1:j+1+length])  # read exactly that many chars
            i = j + 1 + length          # move pointer forward
        return result