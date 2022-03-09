class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [i**2 for i in nums]
        nums.sort()
        return nums
    
    def optimizedSortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = []
        positives = []
        negatives = []
        barrier = 0

        for indx, ele in enumerate(nums):
            if ele < 0:
                barrier+=1
            else:
                positives.append(ele**2)

        for indx in range(barrier-1,-1,-1):
            negatives.append(nums[indx]**2)
        
        pos_indx, neg_indx = 0, 0

        while pos_indx < len(positives) and neg_indx < len(negatives):
            if positives[pos_indx] == negatives[neg_indx]:
                squares.extend([positives[pos_indx], negatives[neg_indx]])
                pos_indx += 1
                neg_indx += 1
            elif positives[pos_indx] < negatives[neg_indx]:
                squares.append(positives[pos_indx])
                pos_indx += 1
            else:
                squares.append(negatives[neg_indx])
                neg_indx += 1

        while pos_indx < len(positives):
            squares.append(positives[pos_indx])
            pos_indx += 1
        
        while neg_indx < len(negatives):
            squares.append(negatives[neg_indx])
            neg_indx += 1

        return squares