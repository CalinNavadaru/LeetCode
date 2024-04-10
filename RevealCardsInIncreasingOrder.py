from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = [0 for _ in range(len(deck))]
        queue = []
        for i in range(len(deck)):
            queue.append(i)

        deck.sort()
        for card in deck:
            result[queue[0]] = card
            queue.pop(0)
            if queue:
                queue.append(queue[0])
                queue.pop(0)

        return result
