class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        output = 0
        for string in s:
            if string == 'L':
                count -= 1
            else:
                count += 1
            if count == 0:
                output += 1
        return output