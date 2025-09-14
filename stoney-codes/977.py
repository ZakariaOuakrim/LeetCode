class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:   # all positive
            return [n*n for n in nums]
        
        # find the first non-negative index
        splitIndex = 0
        for i, n in enumerate(nums):
            if n >= 0:
                splitIndex = i
                break
        
        # split negative and positive parts
        negatif = nums[:splitIndex]    # negative numbers
        positif = nums[splitIndex:]    # non-negative numbers

        # make negative part positive and square them
        negatif = [n*n for n in reversed(negatif)]  # reverse to make ascending
        positif = [n*n for n in positif]

        # merge two sorted lists
        a = b = 0
        merged_list = []

        while a < len(negatif) and b < len(positif):
            if negatif[a] < positif[b]:
                merged_list.append(negatif[a])
                a += 1
            else:
                merged_list.append(positif[b])
                b += 1

        # append remaining elements
        while a < len(negatif):
            merged_list.append(negatif[a])
            a += 1

        while b < len(positif):
            merged_list.append(positif[b])
            b += 1

        return merged_list
