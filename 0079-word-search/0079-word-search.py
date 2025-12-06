class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # terminating condition: k == len(word)
        # start dfs for every location in the grid if grid[i][j] == word[k] when k = 0
        
        def dfs(board, word, i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'

            result = dfs(board, word, i+1, j, k+1) or dfs(board, word, i-1, j, k+1) or dfs(board, word, i, j-1, k+1) or dfs(board, word, i, j+1, k+1)
            
            board[i][j] = tmp
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        
        return False
        
        
