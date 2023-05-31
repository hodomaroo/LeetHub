class UndergroundSystem:

    def __init__(self):
        #timetable // a -> b
        
        self.board = defaultdict(defaultdict)    
        self.log = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.log[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        print(self.log[id])
        st, time = self.log[id]
        self.log[id] = []
        
        if stationName not in self.board[st]:
            self.board[st][stationName] = [0,0]
        self.board[st][stationName][0] += t - time
        self.board[st][stationName][1] += 1
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.board[startStation][endStation][0] / self.board[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)