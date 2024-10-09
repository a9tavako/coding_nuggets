class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b

        if not b:
            return a

        a = a[::-1]
        b = b[::-1]

        shorter = a if len(a) < len(b) else b
        longer = b if shorter == a else a

        first_len = len(shorter)
        second_len = len(longer)
        ans = [0] * (second_len + 1)
        
        for i in range(first_len):
            ans[i] = int(a[i]) + int(b[i])

        for i in range(first_len, second_len):
            ans[i] = int(longer[i])

        for i in range(len(ans)):
            val = ans[i]
            if val >= 2:
                ans[i] -= 2
                ans[i+1] += 1
    
        if ans[-1] == 0:
            ans.pop()

        ans.reverse()

        return "".join(str(d) for d in ans)