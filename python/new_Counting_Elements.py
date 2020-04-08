from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for a in set(arr):
            if a+1 in arr:
                count += arr.count(a)

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countElements([1,1,2,2,3]))