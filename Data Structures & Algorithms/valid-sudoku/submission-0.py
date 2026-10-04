class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_cols, num_rows = len(board[0]), len(board)

        for row in board:
            if not self.isValidCollection(row):
                return False

        for col in range(num_cols):
            column = [board[row][col] for row in range(num_rows)]
            if not self.isValidCollection(column):
                return False

        # iterate through boxes 
        for top_row in range(0, 9, 3):
            for left_col in range(0, 9, 3):
                collection = self.getBoxCollection(board, top_row, left_col)
                if not self.isValidCollection(collection):
                    return False

        return True

    def getBoxCollection(self, board: List[List[str]], row: int, col: int) -> bool:
        collection = []

        for curr_row in range(row, row + 3):
            for curr_iter in range(col, col + 3):
                collection.append(board[curr_row][curr_iter])

        return collection


    def isValidCollection(self, collection: List[str]) -> bool:
        char_set = set()

        for c in collection:
            if c in char_set and c != ".":
                return False
            
            char_set.add(c)

        return True