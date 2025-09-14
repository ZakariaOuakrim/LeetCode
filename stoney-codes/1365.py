class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        dict={}
        for i in range(0,len(sorted_nums)):
            if sorted_nums[i] not in dict:
                dict[sorted_nums[i]]=i
        result=[]
        for n in nums:
            result.append(dict[n])
        return result