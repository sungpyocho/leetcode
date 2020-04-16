from typing import List

class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones = sorted(stones)[::-1]
#         while (len(stones) >= 2):
#             crashed_stone = stones[0] - stones[1]
#             del stones[:2]
            
#             if crashed_stone is not 0:
#                 stones.insert(0, crashed_stone)
                
#             if len(stones) == 0:
#                 return 0
#             if len(stones) == 1:
#                 return stones[0]
            
#             if stones[0] < stones[1]:
#                 stones = sorted(stones)[::-1]
#         return stones[0]

    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     h = [-x for x in A]
    #     heapq.heapify(h)
    #     while len(h) > 1 and h[0] != 0:
    #         heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
    #     return -h[0]
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            # Pop out the two biggest, push back the difference
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0]