"""
Problem: Two Sum
Pattern: Arrays & Hashing
"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    #init hash map
    seen = {}

    #keep track of index and num
    for i, num in enumerate(nums):

        #calc the complement
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    #return empty list for safe fallback
    return []