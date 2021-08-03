# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
# 返回删除后的链表的头节点。
#
# 注意：此题对比原题有改动
#
# 示例 1:
#
# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:
#
# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#  
#
# 说明：
#
# 题目保证链表中节点的值互不相同
# 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 判断一下头节点是不是目标节点
        if head.val == val:
            # 如果是就返回head.next作为新的头节点
            return head.next

        # 双指针设置头节点和当前节点
        pre = head
        cur = head.next

        # 遍历查一下目标节点，条件：当前节点不为null且val相等就跳出循环
        while cur and cur.val != val:
            # 否则更新一下指针位置
            pre = cur
            cur = cur.next

        # 找到了目标节点
        if cur:
            # 更新一下连接
            pre.next = cur.next

        # 返回头节点
        return head
