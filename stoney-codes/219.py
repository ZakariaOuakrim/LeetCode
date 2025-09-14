class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L,R=0,1
        hashSet=set()
        hashSet.add(nums[0])
        while L<R and R<len(nums):
            if R-L>k:
                hashSet.remove(nums[L])
                L+=1
            if nums[R] not in hashSet:
                hashSet.add(nums[R])
                R+=1
            else:
                return True
        return False
             