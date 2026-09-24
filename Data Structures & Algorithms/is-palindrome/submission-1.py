class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_s = ""
        for x in s:
            if x.isalnum():
                check_s += x.lower()
        return check_s == check_s[::-1]