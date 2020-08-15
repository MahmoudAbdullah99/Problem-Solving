class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ls1 = nums[:n]
        ls2 = nums[n:]
        ls3 = []
        for i in range(n):
            ls3.append(ls1[i])
            ls3.append(ls2[i])
        return ls3
        