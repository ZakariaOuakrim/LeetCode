class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=set(nums)
        missing_numbers=[]
        for i in range(1,len(nums+1)):
            if i not in s :
                missing_numbers.append(i)
        
        return missing_numbers