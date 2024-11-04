class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t or len(s) > len(t):
            return False

        s_index = 0
        t_index  = 0

        while s_index < len(s):
            char = s[s_index]
            while t_index <= len(t)-1 and t[t_index] != char:
                t_index += 1

            if t_index == len(t):
                return False

            s_index += 1
            t_index += 1

        return True
        

        