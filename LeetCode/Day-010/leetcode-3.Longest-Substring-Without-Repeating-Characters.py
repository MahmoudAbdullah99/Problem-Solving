class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring_count = 0
        temp_length = 0
        longest_substring = {}
        
        for indx in range(len(s)):
            if not longest_substring.get(s[indx]):
                longest_substring[s[indx]] = indx+1
                temp_length += 1
                
            else:
                temp_length =  min(temp_length+1, (indx+1) - longest_substring[s[indx]])
                longest_substring[s[indx]] = indx+1
            
            if temp_length > longest_substring_count:
                    longest_substring_count = temp_length
                    
        return longest_substring_count
