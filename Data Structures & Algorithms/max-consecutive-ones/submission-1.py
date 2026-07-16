class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum = 0
        largest = 0

        for n in nums:
            if n:
                sum += 1
            else:
                if largest < sum:
                    largest = sum
                sum = 0
        if largest < sum:
            largest = sum
        return largest