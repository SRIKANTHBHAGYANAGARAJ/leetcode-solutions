"""
4. Median of Two Sorted Arrays
Difficulty: Hard
Topics: Array, Binary Search, Divide and Conquer

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
Time Complexity: O(log(min(m, n)))
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary Search Approach (Optimal)
        Time: O(log(min(m, n))), Space: O(1)
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            # Partition position in nums1
            partition1 = (left + right) // 2
            # Corresponding partition in nums2
            partition2 = half_len - partition1
            
            # Handle edge cases
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found correct partition
                if (m + n) % 2 == 0:
                    # Even total length
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    # Odd total length
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # Too far right in nums1, move left
                right = partition1 - 1
            else:
                # Too far left in nums1, move right
                left = partition1 + 1
        
        # Should never reach here with valid input
        raise ValueError("Input arrays are not sorted properly")
    
    def findMedianSortedArrays_simple(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Simple Merge Approach (Not optimal for interview)
        Time: O(m+n), Space: O(m+n)
        """
        merged = []
        i, j = 0, 0
        
        # Merge two sorted arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # Find median
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]
    
    def findMedianSortedArrays_optimized(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Two-pointer approach without merging entire arrays
        Time: O((m+n)/2) = O(m+n), Space: O(1)
        """
        total_len = len(nums1) + len(nums2)
        mid = total_len // 2
        
        i, j = 0, 0
        prev, curr = 0, 0
        
        # Find the middle element(s)
        for _ in range(mid + 1):
            prev = curr
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    curr = nums1[i]
                    i += 1
                else:
                    curr = nums2[j]
                    j += 1
            elif i < len(nums1):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        
        if total_len % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 60)
    print("Testing Median of Two Sorted Arrays")
    print("=" * 60)
    
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([], [2, 3], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.5),
    ]
    
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        # Test optimal solution
        result = solution.findMedianSortedArrays(nums1, nums2)
        
        print(f"\nTest {i}: nums1={nums1}, nums2={nums2}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        
        # Test all three methods
        result1 = solution.findMedianSortedArrays(nums1, nums2)
        result2 = solution.findMedianSortedArrays_simple(nums1, nums2)
        result3 = solution.findMedianSortedArrays_optimized(nums1, nums2)
        
        all_match = (
            abs(result1 - expected) < 0.00001 and
            abs(result2 - expected) < 0.00001 and
            abs(result3 - expected) < 0.00001
        )
        
        if all_match:
            print(f"  ✓ All methods PASS")
        else:
            print(f"  ✗ Methods disagree:")
            print(f"    Optimal: {result1}")
            print(f"    Simple:  {result2}")
            print(f"    Optimized: {result3}")
    
    print("\n" + "=" * 60)
    print("Interactive Testing")
    print("=" * 60)
    
    # Interactive testing
    while True:
        try:
            nums1_input = input("\nEnter nums1 (comma-separated, or 'quit'): ").strip()
            if nums1_input.lower() == 'quit':
                break
            
            nums2_input = input("Enter nums2 (comma-separated): ").strip()
            
            # Parse inputs
            nums1 = [int(x.strip()) for x in nums1_input.split(',') if x.strip()] if nums1_input else []
            nums2 = [int(x.strip()) for x in nums2_input.split(',') if x.strip()] if nums2_input else []
            
            # Sort inputs (just in case)
            nums1.sort()
            nums2.sort()
            
            result = solution.findMedianSortedArrays(nums1, nums2)
            print(f"Median: {result}")
            
        except ValueError:
            print("Invalid input. Please enter comma-separated integers.")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nGoodbye!")