class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(l, r):
            m = (l+r)//2

            print(f"left is {l}, and right is {r} and middle is {m}")

            if l > r:
                return -1
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return search(l,m-1)
            else:
                return search(m+1,r)

        return search(0,len(nums)-1)