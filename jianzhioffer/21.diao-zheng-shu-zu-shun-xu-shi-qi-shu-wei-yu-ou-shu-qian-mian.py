# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
#  
#
# 示例：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
#  
#
# 提示：
#
# 0 <= nums.length <= 50000
# 1 <= nums[i] <= 10000
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        head = 0
        tail = len(nums) - 1
        for n in nums:
            if n % 2 == 1:
                res[head] = n
                head += 1
            else:
                res[tail] = n
                tail -= 1
        return res
