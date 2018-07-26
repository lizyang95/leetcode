class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        bits.pop()
        c = 0
        while bits:
            tmp = bits.pop()
            if tmp == 1:
                c += 1
            else:
                break
        if c % 2 == 0:
            return True
        else:
            return False

class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
