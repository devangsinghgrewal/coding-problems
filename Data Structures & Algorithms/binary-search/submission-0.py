class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # nums=[-1,0,2,4,6,8]
        # target=4

        i = 0
        l = len(nums) - 1 #10, target=7
        m = (i+l)//2 #5

        print(i, l, m)

        while i <= l:
            if target == nums[m]:
                return m
            elif target > nums[m]:
                i = m + 1
            else:
                l = m - 1
            m = (i+l)//2
        return -1
        