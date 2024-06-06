class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize : return False
        
        counter = Counter(hand)
        hand,cur = deque(sorted(hand)),None
        while hand:
            while hand:
                cur = hand.popleft()
                if counter[cur]: break
            
            if not hand: return True
            
            for i in range(groupSize):
                if counter[cur + i] == 0: return False
                counter[cur + i] -= 1
            
        return True
                
