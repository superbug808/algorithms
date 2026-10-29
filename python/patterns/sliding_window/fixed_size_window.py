#Problem: Maximum Sum Subarray of Size K

#Description: Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k

def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        # Add the next element to the window
        window_sum += arr[window_end]
        
        # Once we reach size k, evaluate and slide
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            
            # Subtract element leaving the window
            window_sum -= arr[window_start]

            # Slide the window start forward
            window_start += 1
            
    return max_sum