class Solution:
    def countFreq(self, arr, target):
       
        def first_occurrence(arr, target):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    result = mid
                    high = mid - 1   
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result

       
        def last_occurrence(arr, target):
            low, high = 0, len(arr) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    result = mid
                    low = mid + 1  
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result

        
        first = first_occurrence(arr, target)
        if first == -1:  
            return 0
        last = last_occurrence(arr, target)
        return (last - first + 1)

