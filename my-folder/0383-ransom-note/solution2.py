class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        supply = {}
        for ch in magazine:
            supply[ch] = supply.get(ch, 0) + 1

        for i in ransomNote:
            if i in supply and supply[i] > 0:
                supply[i] -= 1
            else:
                return False
        return True
