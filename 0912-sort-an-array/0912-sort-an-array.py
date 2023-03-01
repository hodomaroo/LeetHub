class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums : List[int]) -> List[int]:
            if len(nums) == 1:  return nums
            a,b = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            pta,ptb = 0,0
            merged = []
            while pta < len(a) and ptb < len(b):
                if a[pta] < b[ptb]:
                    merged.append(a[pta])
                    pta += 1
                else:
                    merged.append(b[ptb])
                    ptb += 1
            while pta < len(a):
                merged.append(a[pta])
                pta += 1

            while ptb < len(b):
                merged.append(b[ptb])
                ptb += 1
            
            return merged

        return merge(nums)