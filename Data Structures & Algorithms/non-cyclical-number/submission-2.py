class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = self.sumOfSquare(n), self.sumOfSquare(self.sumOfSquare(n))

        while slow != fast:
            if fast == 1:
                return True

            slow = self.sumOfSquare(slow)
            fast = self.sumOfSquare(self.sumOfSquare(fast))
            
        return slow == 1

    def sumOfSquare(self, num: int) -> bool:
        square_sum = 0

        while num != 0:
            square_sum += (num % 10) ** 2
            num = num // 10
        
        return square_sum