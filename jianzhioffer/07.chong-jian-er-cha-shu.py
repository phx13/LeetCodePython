# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
#
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
#  
#
# 示例 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 示例 2:
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
#
# 限制：
#
# 0 <= 节点个数 <= 5000
#
#  
#
# 注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 四个参数表示的是这个tree的p左到右，i左到右
        # 比如递归root.left，那么p左到p右表示的是root.left的元素，i左到i右也是表示root.left的元素
        def my_build_tree(p_left, p_right, i_left, i_right):
            if p_left > p_right:
                return None
            # p的第一个肯定是根节点
            p_root_index = p_left
            p_root_val = preorder[p_root_index]
            root = TreeNode(p_root_val)

            # 根据字典找到i的根节点位置
            i_root_index = hash_map[p_root_val]

            i_left_size = i_root_index - i_left

            # 对于root.left
            #     用p来表示就是，root | 左子树 | 右子树，所以左子树的范围是p_left+1到p_left+i_left_size
            #     用i来表示就是，左子树 | root | 右子树，所以左子树的范围是i_left到i_root_index-1
            root.left = my_build_tree(p_left + 1, p_left + i_left_size, i_left, i_root_index - 1)
            root.right = my_build_tree(p_left + i_left_size + 1, p_right, i_root_index + 1, i_right)
            return root

        n = len(preorder)
        hash_map = {item: i for i, item in enumerate(inorder)}
        return my_build_tree(0, n - 1, 0, n - 1)
