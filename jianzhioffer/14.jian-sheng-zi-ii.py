# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#  
#
# 示例 1：
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
#  
#
# 提示：
#
# 2 <= n <= 1000
# 注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/


class Solution:
    def cuttingRope(self, n: int) -> int:
        # 动态规划，dp[n]记录一下长度n的绳子剪完的最大乘积
        # 能知道，dp[2] = 1 * 1 = 1, dp[3] = 1 * 2 = 2, dp[4] = 2 * 2 = 4
        # 所以长度是n的绳子，减掉一段i，剩余长度是n-i，
        # 那么n-i部分可能有两种情况，一种是不裁剪，最后乘积是i*(n-i)；另一种是裁剪，最后乘积是i*dp[n-i]
        # 所以要比较i*(n-i)和i*dp[n-i]哪个大，即dp[n] = max(i*(n-i),i*dp[n-i])

        # # 构建数组
        # dp = [0] * (n + 1)
        # # dp[2]是1
        # dp[2] = 1
        #
        # # 从3开始规划，直到n
        # for x in range(3, n + 1):
        #     # 裁剪长度为i的绳子，2<=i<x，因为如果是裁剪1对乘积没有影响
        #     for i in range(2, x):
        #         # dp[x]的取值是看dp[x]和max(i * (x - i), i * dp[x - i])之间，取最大值
        #         dp[x] = max(dp[x], max(i * (x - i), i * dp[x - i])) % 1000000007
        # return dp[n]

        # 此题和普通剪绳子不同的是需要循环求余，所以贪心算法更适合
        # 几个特殊的值
        # dp[1] = 1
        # dp[2] = 1
        # dp[3] = 2
        # dp[4] = 4
        # 观察贪心算法的规律观察到是
        # 1.绳子长度为3时不能再减，再减乘积会变小
        # 2.剪的越多乘积越大
        # 所以将绳子都剪成长度为3的子绳（除了n=4要剪成2+2）
        if n <= 3:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            res %= 1000000007
            n -= 3
        return n * res % 1000000007
