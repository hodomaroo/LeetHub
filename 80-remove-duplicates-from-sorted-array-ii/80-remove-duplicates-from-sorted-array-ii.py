class Solution(object):
    def removeDuplicates(self, nums):
        cur = None
        cnt = 0
        idx = 0

        for i in range(len(nums)):
            if cur == nums[i]:
                cnt += 1
            elif cur != nums[i]:
                if cur != None:
                    for j in range(min(2,cnt)):
                        nums[j + idx] = cur
                    idx += min(2,cnt)
                cur = nums[i]
                cnt = 1

        for i in range(min(2, cnt)):
            nums[i + idx] = cur
        idx += min(2, cnt)
        return idx