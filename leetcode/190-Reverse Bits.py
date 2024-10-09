class Solution:
    def reverseBits(self, n: int) -> int:
        digits = []
        for _ in range(32):
            if 1 & n == 1:
                digits.append("1")
            else:
                digits.append("0")
            n >>= 1

        return int("".join(digits), 2)