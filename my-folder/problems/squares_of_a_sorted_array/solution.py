class Solution:
    def sortedSquares(self, nums):
        left = []
        right = []

        for index in range(len(nums)):
            if nums[index] < 0:
                left.insert(0, -nums[index])

            if nums[index] >= 0:
                right.extend(nums[index:])
                break
        
        pointer = 0
        for i in range(len(left)):
            while pointer < len(right):
                if left[i] <= right[pointer]:
                    right.insert(pointer, left[i])
                    pointer += 1
                    break
                pointer += 1
            if pointer == len(right):
                right.extend(left[i:])
                break

        return [x ** 2 for x in right]
        