Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

1. Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
*/

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


output:class Solution {
    public int[] twoSum(int[] nums, int target) {

        // Create a HashMap to store numbers and their indices
        Map<Integer, Integer> map = new HashMap<>();
        

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

             if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
 // Store the current number and its index
             map.put(nums[i], i);
        }
        // Since the problem guarantees exactly one solution, we'll never reach here
        return new int[]{};
    }
    }


In python:

"""
1. Two Sum
Difficulty: Easy
Topics: Array, Hash Table

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash Map Solution
        Approach:
        1. Create dictionary to store number-to-index mapping
        2. For each number, calculate complement (target - num)
        3. Check if complement exists in dictionary
        4. If found, return indices, else store current number
        """
        num_map = {}  # {number: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i
        
        return []

# Alternative: Brute Force (O(n^2))
# def twoSum_brute(nums: List[int], target: int) -> List[int]:
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4], 7, [2, 3]),
    ]
    
    for nums, target, expected in tests:
        result = solution.twoSum(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
