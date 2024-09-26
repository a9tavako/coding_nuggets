class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = (1 << 32) + num

        return hex(num)[2:]
