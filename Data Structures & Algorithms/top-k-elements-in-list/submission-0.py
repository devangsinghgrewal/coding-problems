from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        sorted_list = sorted(count.items(), key= lambda x: x[1], reverse= True)[:k]

        return [sl[0] for sl in sorted_list]
