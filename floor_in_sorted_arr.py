class Solution:
    def findFloor(self, arr, x):
        low, high = 0, len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= x:
                result = mid   
                low = mid + 1  
            else:
                high = mid - 1

        return result
