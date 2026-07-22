class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute forcing is slow and O(N^2)
        # Instead we can leap into future and start from right to left

        i = len(arr) - 1
        highest = arr[i]
        arr[i] = -1
        i -= 1

        while i >= 0:
            this_val = arr[i]
            arr[i] = highest
            if this_val > highest:
                highest = this_val
            i -= 1
        
        return arr

