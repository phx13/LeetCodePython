# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
#
#  
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
#
# 提示：
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104
#  
#
# 注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:

        # 第一个错误点，想当然的认为是正数幂，没考虑到负数
        # 第二个错误点，循环超时
        # res = 1
        # if n > 0:
        #     for i in range(n):
        #         res *= x
        #     return res
        # else:
        #     for i in range(-n):
        #         res *= x
        #     return 1 / res

        # 快速幂方法，二进制
        # 十进制的二进制表示：bmbm-1bm-2...b3b2b1
        #                 101...101
        # 十进制转二进制即是n=1*b1+2*b2+4*b3+...+2m-1*bm
        # 所以x^n = x^1*b1+2*b2+4*b3+...+2m-1*bm
        # 根据幂的拆分法则，上述又= (x^1*b1)*(x^2*b2)...
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res


print(Solution().myPow(2, -2))
