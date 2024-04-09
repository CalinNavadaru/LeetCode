from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        steps = 0
        while tickets[k] != 0:
            for i in range(k + 1):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    steps += 1
            if tickets[k] == 0:
                break
            for i in range(k + 1, len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    steps += 1

        return steps
