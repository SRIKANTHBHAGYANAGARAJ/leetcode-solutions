"""
3. Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window Approach
        Time: O(n), Space: O(min(n, m)) where m is character set size
        """
        char_set = set()  # Store characters in current window
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # If duplicate found, shrink window from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to window
            char_set.add(s[right])
            
            # Update maximum length
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        Optimized Sliding Window using dictionary
        Time: O(n), Space: O(min(n, m))
        """
        char_index = {}  # Store last index of each character
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            # If character seen and within current window
            if char in char_index and char_index[char] >= start:
                # Move start to after the duplicate
                start = char_index[char] + 1
            
            # Update character's last index
            char_index[char] = end
            
            # Update maximum length
            current_length = end - start + 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length


# Test function
def test_solution():
    solution = Solution()
    
    print("=" * 60)
    print("Testing Longest Substring Without Repeating Characters")
    print("=" * 60)
    
    test_cases = [
        ("abcabcbb", 3),   # "abc"
        ("bbbbb", 1),      # "b"
        ("pwwkew", 3),     # "wke"
        ("", 0),           # empty string
        (" ", 1),          # single space
        ("au", 2),         # "au"
        ("dvdf", 3),       # "vdf"
        ("abba", 2),       # "ab" or "ba"
        ("tmmzuxt", 5),    # "mzuxt"
    ]
    
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        # Test both methods
        result1 = solution.lengthOfLongestSubstring(s)
        result2 = solution.lengthOfLongestSubstring2(s)
        
        # Both methods should give same result
        if result1 == expected and result2 == expected:
            print(f"Test {i} ✓: \"{s}\" -> {result1}")
        else:
            print(f"Test {i} ✗: \"{s}\"")
            print(f"  Method 1: {result1} (expected: {expected})")
            print(f"  Method 2: {result2} (expected: {expected})")
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("All tests PASSED! ✓")
    else:
        print("Some tests FAILED! ✗")
    print("=" * 60)


# Run tests if this file is executed directly
if __name__ == "__main__":
    test_solution()
    
    # Additional interactive test
    solution = Solution()
    print("\n" + "=" * 60)
    print("Interactive Test")
    print("=" * 60)
    
    while True:
        user_input = input("\nEnter a string (or 'quit' to exit): ").strip()
        if user_input.lower() == 'quit':
            break
        
        result = solution.lengthOfLongestSubstring(user_input)
        print(f"Longest substring without repeating characters: {result}")
        
        # Show the actual substring (optional challenge)
        # This is for demonstration - finds one possible longest substring
        if user_input:
            char_set = set()
            left = 0
            max_start = 0
            max_end = 0
            max_len = 0
            
            for right in range(len(user_input)):
                while user_input[right] in char_set:
                    char_set.remove(user_input[left])
                    left += 1
                
                char_set.add(user_input[right])
                
                if (right - left + 1) > max_len:
                    max_len = right - left + 1
                    max_start = left
                    max_end = right
            
            longest_sub = user_input[max_start:max_end + 1]
            print(f"One possible longest substring: \"{longest_sub}\"")
    
    print("\nGoodbye!")