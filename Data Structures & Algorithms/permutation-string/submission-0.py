class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count = {}
        window = {}

        for char in s1:
            count[char] = count.get(char, 0) + 1

        for char in s2[:len(s1)]:
            window[char] = window.get(char, 0) + 1

        if count == window:
            return True

        l = 0
        r = len(s1)

        while r < len(s2):
            # Remove leftmost character
            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                del window[s2[l]]

            # Add rightmost character
            window[s2[r]] = window.get(s2[r], 0) + 1
            l += 1
            r += 1
            if count == window:
                return True
        return False