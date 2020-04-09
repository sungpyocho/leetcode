# https://leetcode.com/problems/backspace-string-compare/
def TypeKeyboard(arr):
    typed_text = []
    for a in arr:
        if a != '#':
            typed_text.append(a)
        elif typed_text:
            typed_text.pop()
    
    return typed_text

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return TypeKeyboard(S) == TypeKeyboard(T)

if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("ab#c", "ad#cd#")) # True