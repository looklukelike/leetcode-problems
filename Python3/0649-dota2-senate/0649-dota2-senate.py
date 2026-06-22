from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = deque()
        dire = deque()

        for i, senator in enumerate(senate):
            match(senator):
                case 'R':
                    radiant.append(i)
                case 'D':
                    dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"