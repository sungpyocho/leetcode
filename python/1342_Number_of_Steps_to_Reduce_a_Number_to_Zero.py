class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while (num != 0):
            if (num % 2):
                # if num is odd number
                num -= 1
                count +=1
            else:
                num /= 2
                count +=1
        return count
        