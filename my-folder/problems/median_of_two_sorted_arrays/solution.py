import math

class Solution:
        def findMedianSortedArrays(self, left_list: List[int],
                                               right_list: List[int]) -> float:
                            if len(left_list) and len (right_list) and left_list[-1] <= right_list[0]:
                                final = left_list + right_list
                                return final[len(final) // 2] if len(final) % 2 else \
                                    (final[(len(final) // 2) - 1] + final[len(final) // 2]) / 2
                            elif len(left_list) and len (right_list) and right_list[-1] <= left_list[0]:
                                final = right_list + left_list
                                return final[len(final) // 2] if len(final) % 2 else \
                                    (final[(len(final) // 2) - 1] + final[len(final) // 2]) / 2
                            else:
                                length = len(left_list) + len(right_list)
                                half_length = length // 2
                                odd = bool(length % 2)

                                if len(left_list) > len(right_list):
                                    right_list, left_list = left_list, right_list

                                left_index, right_index = 0, len(left_list) - 1
                                while True:
                                    mid_left = (left_index + right_index) // 2
                                    mid_right = half_length - mid_left - 2

                                    left_1 = left_list[mid_left] if mid_left >= 0 else -math.inf
                                    right_1 = left_list[mid_left+1] if mid_left+1 < len(
                                        left_list) else math.inf

                                    left_2 = right_list[mid_right] if mid_right >= 0 else -math.inf
                                    right_2 = right_list[mid_right+1] if mid_right+1 < len(right_list) else math.inf

                                    if left_1 <= right_2 and left_2 <= right_1:
                                        if odd:
                                            return min(right_1, right_2)
                                        else:
                                            return (max(left_1, left_2) + min(right_1, right_2)) / 2
                                    elif left_1 > right_2:
                                        right_index = mid_left - 1
                                    else:
                                        left_index = mid_left + 1
