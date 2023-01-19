class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_count = 0
        temp_length = 0
        chars_indexes = {}

        for index, element in enumerate(s):
            if chars_indexes.get(element) == None:
                temp_length += 1
                chars_indexes[element] = index
            else:
                temp_length = min((index-chars_indexes[element]), temp_length+1)
                chars_indexes[element] = index

            longest_substring_count = max(longest_substring_count, temp_length)

        return longest_substring_count