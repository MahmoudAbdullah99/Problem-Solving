

class Solution(object):
    def binarySearch(self, nums, target, left=None, right=None):
        if left == None:
            left = 0
        
        if right == None:
            right = len(nums)-1
        
        print(nums[left:right+1])
        print(target)
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return
    
    def twoSumBinarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indx1 in range(len(nums)):
            indx2 = self.binarySearch(nums, target-nums[indx1], left=indx1+1)
            print(indx1, indx2)
            if indx2 != None and indx1 != indx2:
                return [indx1+1, indx2+1]
