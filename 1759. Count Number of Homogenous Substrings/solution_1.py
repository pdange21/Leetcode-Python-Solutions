class Solution:
  def countHomogenous(self, s: str) -> int:
    Mod = 10 ** 9 + 7
    ans = 0
    count = 0
    currentChar = '@'

    for c in s:
      count = count + 1 if c == currentChar else 1
      currentChar = c
      ans += count
      ans %= Mod

    return ans
