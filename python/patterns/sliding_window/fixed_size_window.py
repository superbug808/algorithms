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

if __name__ == "__main__":
    # Standard case
    print(f"Test 1 (Standard): {max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])}") 
    # Expected: 9

    # Edge Case: k = 1 (window size of 1)
    print(f"Test 2 (k=1): {max_sub_array_of_size_k(1, [4, 2, 1, 7])}") 
    # Expected: 7

    # Edge Case: k equals array length
    print(f"Test 3 (k == len(arr)): {max_sub_array_of_size_k(4, [1, 2, 3, 4])}") 
    # Expected: 10

    # Edge Case: All negative numbers
    print(f"Test 4 (All Negatives): {max_sub_array_of_size_k(2, [-2, -1, -3, -4])}") 
    # Expected: -3 (from [-2, -1])