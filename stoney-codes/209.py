class Solution:
        def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            if nums[L]==target:
                 return 1

            nums.sort(reverse=True)
            L,R=0,1
            result=0
            numberOfElements=1
            while L<R and R<len(nums):
                if nums[L]+nums[R]>=target:
                    numberOfElements+=1
                    return numberOfElements
                pass
