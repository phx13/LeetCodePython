import functools
from typing import List


# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
#  
#
# 示例 1:
#
# 输入: [10,2]
# 输出: "102"
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: "3033459"
#  
#
# 提示:
#
# 0 < nums.length <= 100
# 说明:
#
# 输出结果可能非常大，所以你需要返回一个字符串而不是整数
# 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 本质是排序，自定义列表的排序，使用functools.cmp_to_key(function)
        # 比较大小即是比较两项转为字符串后的大小，如果l + r > r + l('3,30' > '30,3')，l就排到r后面，这样形成的字符串大小是最小的

        def custom_sort(l, r):
            if l + r > r + l:
                return 1
            else:
                return -1

        str_nums = [str(num) for num in nums]
        str_nums.sort(key=functools.cmp_to_key(custom_sort))
        return ''.join(str_nums)


nums = [10, 5, 3, 4]
print(Solution().minNumber(nums))
