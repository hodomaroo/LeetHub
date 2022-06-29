from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        listUp = [(float("inf"),-1)] * len(people)

        print(people)
        for v, c in people:
            count = 0
            pos = 0
            while count < c or listUp[pos][0] <= v:
                count += listUp[pos][0] >= v
                pos += 1

            listUp[pos] = [v, c]

        return listUp



