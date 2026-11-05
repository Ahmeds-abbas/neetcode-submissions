class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            hours = sum((p + k - 1) // k for p in piles)  # ceil(p/k) without floats
            if hours <= h:
                hi = k        # k works, so try slower
            else:
                lo = k + 1    # too slow
        return lo