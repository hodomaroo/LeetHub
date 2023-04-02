class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions) - bisect_left(potions, success / v) for v in spells]
    #ㅠ >= success인 값을 찾아야 함
    #b >= (success / a)를 만족해야 함
    #b < success / b인 것들의 개수 -> bisect_right(success / a) -> == 도 포함해버림
            
            