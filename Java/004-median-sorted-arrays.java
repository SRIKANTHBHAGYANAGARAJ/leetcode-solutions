class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array for binary search optimization
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int left = 0, right = m;
        
        while (left <= right) {
            // Partition nums1
            int partition1 = (left + right) / 2;
            // Partition nums2 (formula ensures equal elements on both sides)
            int partition2 = (m + n + 1) / 2 - partition1;
            
            // Handle edge cases for left and right values
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            
            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];
            
            // Check if we found the correct partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Found the correct partition
                if ((m + n) % 2 == 0) {
                    // Even total length: average of two middle elements
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                } else {
                    // Odd total length: middle element
                    return Math.max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                // Too far right in nums1, move left
                right = partition1 - 1;
            } else {
                // Too far left in nums1, move right
                left = partition1 + 1;
            }
        }
         // Should never reach here with valid input
        throw new IllegalArgumentException("Input arrays are not sorted properly");
    }}
    