class Solution(object):
    def minDistance(self, word1, word2):
        def find(i, j, memo):
            if i == len(word1) and j == len(word2):
                return 0
            
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if (i, j) not in memo:  #현재 위치에서의 최솟값을 리턴함이 보장됨
                if word1[i] == word2[j]:
                    ans = find(i+1, j+1, memo)
                else:
                    add = 1 + find(i, j+1, memo) # add
                    delete = 1 + find(i+1, j, memo) # delete
                    replace = 1 + find(i+1, j+1, memo)
                    ans = min(add, delete, replace)
                memo[(i,j)] = ans
            return memo[(i,j)]
        return find(0, 0, {})