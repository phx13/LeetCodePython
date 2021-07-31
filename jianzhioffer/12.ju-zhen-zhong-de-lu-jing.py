# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#
#
#
#  
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
#
# 提示：
#
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# board 和 word 仅由大小写英文字母组成
#  
#
# 注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度优先搜索
        # DFS解析：
        #
        # 递归参数：
        # 当前元素在矩阵board中的行列索引i和j ，当前目标字符在word中的索引k 。
        #
        # 终止条件：
        # 返回falsefalse ： (1)行或列索引越界或(2)当前矩阵元素与目标字符不同或(3)当前矩阵元素已访问过 （ (3)可合并至(2) ） 。
        # 返回truetrue ： k = len(word) - 1 ，即字符串word已全部匹配。
        #
        # 递推工作：
        # 标记当前矩阵元素： 将board[i][j]修改为空字符'' ，代表此元素已访问过，防止之后搜索时重复访问。
        # 搜索下一单元格： 朝当前元素的上、下、左、右四个方向开启下层递归，使用或连接 （代表只需找到一条可行路径就直接返回，不再做后续DFS ），并记录结果至res 。
        # 还原当前矩阵元素： 将board[i][j]元素还原至初始值，即word[k] 。
        #
        # 返回值： 返回布尔量res ，代表是否搜索到目标字符串。
        def dfs(r, c, index):
            # 如果超出矩阵，或者字符不相等，返回false
            if not 0 <= r < rows or not 0 <= c < cols or board[r][c] != word[index]:
                return False
            # 如果一直查到最后一个索引，证明找到了，返回true
            if index == len(word) - 1:
                return True

            # 查到了之后把当前位置设置成‘’，代表走过了，再去查下一个
            board[r][c] = ''

            # 查四个方位，找到任意一个就返回true
            res = dfs(r, c - 1, index + 1) or dfs(r, c + 1, index + 1) or dfs(r - 1, c, index + 1) or dfs(r + 1, c, index + 1)

            # 把当前位置在恢复字符
            board[r][c] = word[index]
            return res

        cols = len(board[0])
        rows = len(board)
        index = 0
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, index):
                    return True
        return False
