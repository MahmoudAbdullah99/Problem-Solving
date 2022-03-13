class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        indx_1, indx_2, pointer = 0, 0, m

        if m == 0:
            nums1[:] = nums2
            return
        elif n == 0:
            return
        
        while indx_1 < m and indx_2 < n:
            if nums1[indx_1] <= nums2[indx_2]:
                if pointer < m+n:
                    nums1[pointer] = nums1[indx_1]
                else:
                    nums1.append(nums1[indx_1])
                indx_1 += 1
            else:
                if pointer < m+n:
                    nums1[pointer] = nums2[indx_2]
                else:
                    nums1.append(nums2[indx_2])
                indx_2 += 1
            pointer += 1

        while pointer < len(nums1):
            nums1.pop()
                
        if indx_1 < m:
            nums1.extend(nums1[indx_1:m])
        
        if indx_2 < n:
            diff = n-indx_2
            nums1.extend(nums2[indx_2:n])
        
        nums1[:] = nums1[m:]