from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        count_s = Counter(S)
        for i in J:
            counter += count_s[i]
        return counter