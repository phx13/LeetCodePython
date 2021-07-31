# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#  
#
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：
#
# 1 <= n,m <= 100
# 0 <= k <= 20
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 计算一下数位和
        def calculate(i, j):
            res = 0
            while i > 0:
                res += i % 10
                i //= 10
            while j > 0:
                res += j % 10
                j //= 10
            return res

        def dfs(i, j):
            # 三种情况不增加结果
            # 1. 超出矩阵了
            # 2. 数位和>k
            # 3. 访问过了
            if not 0 <= i < m or not 0 <= j < n or calculate(i, j) > k or (i, j) in board:
                return 0

            # 否则就记录进来
            board.add((i, j))

            # 从(0,0)点开始，向右和向下去搜索，数量加1
            return dfs(i + 1, j) + dfs(i, j + 1) + 1

        # 辅助矩阵
        board = set()
        return dfs(0, 0)
