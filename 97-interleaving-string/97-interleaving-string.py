class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        stageSet = {0} #현재 사용 가능한 위치

        for i in range(len(s3)):
            nextSet = set()
            print(stageSet)

            for index in stageSet:
                if index < len(s2) and s3[i] == s2[index]:
                    nextSet.add(index + 1)
                if i - index < len(s1) and s3[i] == s1[i - index]:
                    nextSet.add(index)

            stageSet = nextSet.copy()
        
        return True if stageSet else False




