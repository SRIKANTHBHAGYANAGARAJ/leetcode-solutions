/*
3. Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Given a string s, find the length of the longest substring without repeating characters.
*/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Sliding window approach
        Set<Character> set = new HashSet<>();
        int maxLength = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // If character is in set, move left pointer
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            
            // Add current character to set
            set.add(s.charAt(right));
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
    
    // Alternative: Using HashMap for faster lookups
    public int lengthOfLongestSubstring2(String s) {
        // HashMap to store character indices
        int[] lastIndex = new int[256]; // ASCII extended
        Arrays.fill(lastIndex, -1);
        
        int maxLength = 0;
        int start = 0;
        
        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            
            // If character seen and within current window
            if (lastIndex[c] >= start) {
                start = lastIndex[c] + 1;
            }
            
            // Update last index of character
            lastIndex[c] = end;
            
            // Update max length
            maxLength = Math.max(maxLength, end - start + 1);
        }
        
        return maxLength;
    }
    
    // Main method for testing (remove for LeetCode)
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test cases
        String[] testCases = {
            "abcabcbb",  // Expected: 3
            "bbbbb",     // Expected: 1
            "pwwkew",    // Expected: 3
            "",          // Expected: 0
            " ",         // Expected: 1
            "au",        // Expected: 2
            "dvdf"       // Expected: 3
        };
        
        int[] expected = {3, 1, 3, 0, 1, 2, 3};
        
        for (int i = 0; i < testCases.length; i++) {
            int result = solution.lengthOfLongestSubstring(testCases[i]);
            System.out.println("Test " + (i + 1) + ": \"" + testCases[i] + "\"");
            System.out.println("  Result: " + result);
            System.out.println("  Expected: " + expected[i]);
            System.out.println("  " + (result == expected[i] ? "✓ PASS" : "✗ FAIL"));
            System.out.println();
        }
    }
}





////////////////

import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int left = 0, maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // If character at right is already in set, move left pointer
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            // Add current character to set
            set.add(s.charAt(right));
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}