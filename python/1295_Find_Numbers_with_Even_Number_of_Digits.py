from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def findDigits (nums): 
            digits = 1
            while(nums >= 10):
                nums = nums // 10
                digits += 1
            return digits
        
        return sum([findDigits(n) % 2 == 0 for n in nums])