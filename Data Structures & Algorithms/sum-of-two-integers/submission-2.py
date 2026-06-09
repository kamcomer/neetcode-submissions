class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF
        for bit in range(32):
            aBit = (a >> bit) & 1
            bBit = (b >> bit) & 1

            curBit = aBit ^ bBit ^ carry
            carry = (aBit + bBit + carry) >= 2

            if curBit:
                res |= (1 << bit)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res

