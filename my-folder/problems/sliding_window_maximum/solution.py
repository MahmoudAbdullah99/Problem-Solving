from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        max_q = deque()
        res = []
        l = 0
        
        for r, element in enumerate(nums):
            
            while max_q and nums[max_q[-1]] < element:
                max_q.pop()
            
            max_q.append(r)
            
            if r-k+1 >= 0:
                res.append(nums[max_q[0]])

            if r-k+1 >= max_q[0]:
                max_q.popleft()
            
    
        return res