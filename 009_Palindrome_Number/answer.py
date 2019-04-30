class Solution:
    def isPalindrome(self, number: int) -> bool:
        number = str(number)

        if number[::-1] != number:
            return False
        return True