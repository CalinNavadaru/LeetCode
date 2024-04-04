class Solution:

    def exits_aux(self, i, j, index, board, word):
        if index >= len(word) - 1:
            return True

        temp = board[i][j]
        board[i][j] = ''
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        ok = False
        for x, y in zip(dx, dy):
            if not (0 <= i + x < len(board)) or not (0 <= j + y < len(board[0])):
                continue
            if board[i + x][j + y] == word[index + 1]:
                ok = ok or self.exits_aux(i + x, j + y, index + 1, board, word)
                if ok == True:
                    return True

        board[i][j] = temp
        return ok

    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    if self.exits_aux(i, j, 0, board, word):
                        return True

        return False
