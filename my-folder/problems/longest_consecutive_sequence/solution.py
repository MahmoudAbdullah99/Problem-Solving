class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        hashset = set(nums)        
        
        for num in nums:
            if num-1 in hashset:
                continue
            
            temp_length = 1
            while num+temp_length in hashset:
                temp_length += 1
            longest_seq = max(longest_seq, temp_length)
                        
        return longest_seq