class Solution:
    def longestPalindrome(self, s: str):
        def helper(left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left + 1: right]
        result = ''
        for i in range(len(s)):
            test = helper(i, i)
            if len(test) > len(result):
                result = test
            test = helper(i, i+1)
            if len(test) > len(result):
                result = test
        return result


ans = Solution()
print(ans.longestPalindrome('bobad'))
