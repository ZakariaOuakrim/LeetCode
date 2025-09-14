class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x,y,z=0,1,2
        sum=0
        nums.sort()
        result=[]
        while (x<y and y<z) and z<len(nums):
            sum = nums[x]+nums[y]+nums[z]
            if sum==0:
                result.append([nums[x],nums[y],nums[z]])
            elif sum>0:
                pass
            else:
                pass