class Solution(object):
    def lengthOfLongestSubstringHashTable(self, s):
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

            longest_substring_count = max(temp_length, longest_substring_count)
            
        return longest_substring_count
    
    def lengthOfLongestSubstringHashTableOptimized(self, s):
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
                if temp_length+1 < ((indx+1) - longest_substring[s[indx]]):
                    temp_length += 1
                else:
                    temp_length = (indx+1) - longest_substring[s[indx]]
                
                longest_substring[s[indx]] = indx+1
            
            if temp_length > longest_substring_count:
                    longest_substring_count = temp_length
            
        return longest_substring_count
