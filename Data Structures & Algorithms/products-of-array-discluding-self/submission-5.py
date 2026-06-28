class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        target = []
        product = 1
        zeroes = []
        for i,n in enumerate(nums):
            if n !=0:
                product = product*n
            else:
                zeroes.append(i)

        if len(zeroes) == len(nums):
            product = 0
        
        for i,n in enumerate(nums):
            if n !=0 and not zeroes:
                target.append(int(product/n))
            elif n !=0 and zeroes:
                target.append(0)
            elif n == 0 and len(zeroes) > 1:
                target.append(0)
            else:
                target.append(product)
        
        return target

