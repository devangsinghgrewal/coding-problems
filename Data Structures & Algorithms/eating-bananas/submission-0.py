import numpy as np
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def _can_finish(piles, h, k):
            return sum(np.ceil(p/k) for p in piles) <=h
        
        l, r = 1, max(piles)

        while l <r:
            m = (l+r)//2

            if _can_finish(piles, h, m):
                r = m # try smaller
            else:
                l = m + 1
            
        return l        