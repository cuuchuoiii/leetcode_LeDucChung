#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      i = 0
      a = []
      for j in range(len(nums)):
        if nums[j] == val:
            a.append(nums[j])
        else:
            nums[i] = nums[j]
            i += 1
      return i
# @lc code=end

