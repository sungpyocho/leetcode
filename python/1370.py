class Solution:
    def sortString(self, s: str) -> str:
        string = sorted(s)
        result = ""
        flag = 0
        
        while string:
            str_set = sorted(set(string))
            flag ^= 1
            if flag:
                for s in str_set:
                    string.remove(s)
                    result += s
            else:
                for s in str_set[::-1]:
                    string.remove(s)
                    result += s
        
        return result