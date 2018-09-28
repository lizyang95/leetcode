class Solution:
    def backPack(self, w, v, C):
        '''
        :param w: list
        :param v: list
        :param C: int 背包最大容量
        :return: int
        '''
        n = len(w)
        if n == 0 or C == 0:
            return 0
        row = [-1 for i in range(C+1)]
        memo = [row.copy() for i in range(n)]
        # 第一行计算
        for i in range(C+1):
            if i >= w[0]:
                memo[0][i] = v[0]
            else:
                memo[0][i] = 0

        for i in range(1, n):  # 增加i个物品后的最优化计算
            for j in range(C+1):  # 第i个物品 第j个位置的最大价值
                if j >= w[i]:
                    memo[i][j] = max(v[i]+memo[i-1][j-w[i]], memo[i-1][j])
                else:  # j < w[i]
                    memo[i][j] = memo[i-1][j]
        return memo[n-1][C]

# 测试
w = [1,2,3]
v = [6,10,12]
C = 5
print(Solution().backPack(w, v,C))
