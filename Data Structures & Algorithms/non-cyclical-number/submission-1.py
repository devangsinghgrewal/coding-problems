class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(number):
            sum_number = 0
            while number >0:
                rem = number % 10
                digit = rem*rem
                sum_number += digit

                number = number // 10
            return sum_number
        
        slow = n
        fast = sum_of_squares(n)

        while fast!=1 and slow!=fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
        
        return fast == 1