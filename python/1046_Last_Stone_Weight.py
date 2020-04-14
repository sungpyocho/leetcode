class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)[::-1]
        while (len(stones) > 1):
            del stones[:2]
            stones.insert(0, stones[0] - stones[1])
            
            if stones[0] < stones[1]:
                stones = sorted(stones)[::-1]
            print(stones)