class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers)-1

        while left_pointer < len(numbers) and right_pointer >= -1:
            if numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            elif numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            else:
                return [left_pointer+1, right_pointer+1]