from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def ConvertedHashValue(hash : int):
            hashVal = []
            while hash:
                hashVal.append(chr(hash % 100 + 55))
                hash //= 100
            return hashVal[::-1]

        hashCounter = Counter()
        if len(s) <= 10: return []
        else:
            hashVal = 0
            for i in range(10):
                hashVal = hashVal * 100 + ord(s[i]) - 55
            hashCounter[hashVal] += 1

            for i in range(10,len(s)):
                hashVal = hashVal % pow(10,18) * 100 + ord(s[i]) - 55
                hashCounter[hashVal] += 1
        
        return ["".join(ConvertedHashValue(v)) for v in hashCounter if hashCounter[v] >= 2]

