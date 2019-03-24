#! /bin/env python3


class BitMask(int):
    def AND(self, bm):
        return BitMask(self & bm)

    def OR(self, bm):
        return BitMask(self | bm)

    def XOR(self, bm):
        return BitMask(self ^ bm)

    def NOT(self):
        return BitMask(~self)

    def shiftleft(self, num):
        return BitMask(self << num)

    def shiftright(self, num):
        return BitMask(self > num)

    def bit(self, num):
        mask = 1 << num
        return bool(self & mask)

    def setbit(self, num):
        mask = 1 << num
        return BitMask(self | mask)

    def zerobit(self, num):
        mask = ~(1 << num)
        return BitMask(self & mask)

    def listbits(self, start=0, end=-1):
        end = end if end < 0 else end + 2
        return [int(c) for c in bin(self)[start + 2 : end]]
