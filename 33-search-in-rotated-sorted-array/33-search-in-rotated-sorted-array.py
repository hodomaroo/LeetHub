from bisect import bisect_left

class Solution(object):
    def search(self, nums, target):

        left,right = 0,len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            #print(left,right)
            if nums[mid] == target: return mid

            if (nums[right] < nums[mid] and (target > nums[mid] or target <= nums[right])) or \
                    nums[mid] < target <= nums[right]:    left = mid + 1
            else: right = mid - 1
        return -1