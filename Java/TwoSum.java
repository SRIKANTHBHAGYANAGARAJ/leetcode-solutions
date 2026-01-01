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
