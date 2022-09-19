class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #pathString 분할 (" ")
        #-> 0 : 경로정보 / ELSE : 파일
        
        fileGroup = defaultdict(list)
        
        def getInformationOfFile(info : str) -> list[str]:
            info = info.split(".")
            fileName = info[0]
            info = info[1].split("(")
            fileExpe = info[0]
            fileContents = info[1][:-1]
            
            return [fileName, fileExpe, fileContents]
                
        #print(getInformationOfFile("1.txt(abcd)"))
        
        for path in paths:
            route, *files = path.split()
            
            for file in files:
                name,expe, contents = getInformationOfFile(file)
                fileGroup[contents].append(route + "/" + name + "." + expe)
        
        return [fileGroup[contents] for contents in fileGroup if len(fileGroup[contents]) > 1]
            