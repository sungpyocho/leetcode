# https://leetcode.com/problems/single-number/
from typing import List

class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     result = 0
    #     for num in nums:
    #         result ^= num
    #     return result

    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))