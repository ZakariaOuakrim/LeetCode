class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index,number in enumerate(nums):
            if target-number in dict:
                return index,dict[target-number]
            else:
                dict[number]=index