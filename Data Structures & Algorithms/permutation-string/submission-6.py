class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)< len(s1):
            return False

        count = {}
        word = {}    

        for i in s1:
            count[i] = count.get(i, 0) + 1
        for i in s2[:len(s1)]:
            word[i] = word.get(i, 0) + 1

        if word == count:
            return True

        l = 0
        r = len(s1)
        while r < len(s2):
          word[s2[l]] -= 1
          if word[s2[l]] == 0:
                del word[s2[l]]
          word[s2[r]] = word.get(s2[r], 0) + 1
          l += 1
          r += 1
          if word == count:
            return True
        return False    
      

