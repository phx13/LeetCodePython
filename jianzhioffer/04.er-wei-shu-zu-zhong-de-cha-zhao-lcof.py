from typing import List


# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
#  
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
#
#  
#
# 限制：
#
# 0 <= n <= 1000
#
# 0 <= m <= 1000
#
#  
#
# 注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 同一行左比右小，同一列上比下小，所以可以从右上角出发，右上角即是这一行最大的，也是这一列最小的
        # 所以只要目标比当前大，就向下一行；目标比当前小，就向左一列
        # 直到超出矩阵返回false，或者找到目标返回true
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height = len(matrix)
        width = len(matrix[0])

        row = 0
        col = width - 1

        while row < height and col >= 0:
            if matrix[row][col] > target:
                col = col - 1
            elif matrix[row][col] < target:
                row = row + 1
            elif matrix[row][col] == target:
                return True
        return False
