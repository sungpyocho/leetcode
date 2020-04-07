# https://leetcode.com/problems/maximum-subarray/
from typing import List

class Solution:
    # Dynamic Programming을 사용
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))