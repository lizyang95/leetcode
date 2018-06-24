class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # directions = 'RLUD'
        # counts = {char:0 for char in directions}
        # for i in range(len(moves)):
        #     counts[moves[i]] += 1
        # if counts['R'] == counts['L'] and counts['U'] == counts['D']:
        #     return True
        # else:
        #     return False
        return (moves.count('L') == moves.count('R')) and (moves.count('U')==moves.count('D'))


def main():
    sol = Solution()
    # moves = 'LL'
    moves = ''
    print(sol.judgeCircle(moves))

if __name__ == '__main__':
    main()
