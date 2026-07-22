class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        # Get a value from list
        # Subtract it from the target
        # Check if the resulting value is already in hashmap
        # If found, return the current index and a value (representing index) of hashmap
        # Else store the current value as index and current index as hashmap's value

        for i in range(len(nums)):
            if map.get(target - nums[i], None) != None:
                return [map.get(target - nums[i], 0), i]
            else:
                map[nums[i]] = i