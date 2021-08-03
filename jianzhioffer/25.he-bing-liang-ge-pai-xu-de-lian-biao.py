# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
#
# 0 <= 链表长度 <= 1000
#
# 注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        res = head

        p1 = l1
        p2 = l2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                res.next = p1
                res = res.next
                p1 = p1.next
            else:
                res.next = p2
                res = res.next
                p2 = p2.next

        if p1:
            res.next = p1

        if p2:
            res.next = p2

        return head.next
