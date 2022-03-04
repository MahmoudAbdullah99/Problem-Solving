"""Problem Description:
    - You are a product manager and currently leading a team to develop a new
    product. Unfortunately, the latest version of your product fails the
    quality check. Since each version is developed based on the previous
    version, all the versions after a bad version are also bad.
    - Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad. You are
    given an API bool isBadVersion(version) which returns whether version is
    bad.
    - Implement a function to find the first bad version. You should minimize
    the number of calls to the API.

Notes:
    - There is a no array, you are given a number->int representing the
    number of the versions.
    - The problem is similar to the binary search approach, but you return the index where it
    the first bad version.
    - Detecting the bad version can be done by searching iteratively for the
    last bad version in the sublist of the good versions (right to bad version).

Steps:
    - Search using the binary search approach, and get the result of
isBadVersion function:
        - If the answer is true then we need to search the left sublist; the
        first bad version is in the left of the current version or it is the
        current version.
        - If the answer is false then we need to search the left sublist; the
        first bad version is in the right of the current version.

TODO:
    - Review.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(version):
    return


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1

        left, right = 1, n

        while left <= right:
            version = (left + right) // 2

            if isBadVersion(version):
                right = version - 1
            else:
                left = version + 1

        return left
