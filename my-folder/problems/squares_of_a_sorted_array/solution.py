class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i, j = 0, len(A)-1
        c = len(A)-1
        sq_nums = [0] * len(A)

        while c >= 0:
            left_sq = A[i] ** 2
            right_sq = A[j] ** 2

            if left_sq >= right_sq:
                sq_nums[c] = left_sq
                i += 1
            else:
                sq_nums[c] = right_sq
                j -= 1
            c -= 1

        return sq_nums