class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = defaultdict(list)

        new_rows = rows + 1

        for i in range(65, 91):
            self.spreadsheet[chr(i)] = [0] * new_rows   
        
    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:])

        self.spreadsheet[col][row] = value        

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:])

        self.spreadsheet[col][row] = 0

    def getValue(self, formula: str) -> int:
        formula_arr = formula[1:].split('+')
        
        result = 0

        def get_value_helper(cell: str):
            row = cell[0]
            col = int(cell[1:])

            return int(self.spreadsheet[row][col])

        # '=5+7'
        if formula_arr[0].isdigit() and formula_arr[1].isdigit():
            result = int(formula_arr[0]) + int(formula_arr[1])
        elif formula_arr[0].isdigit():
            # get row and col from formula_arr[1]
            val = get_value_helper(formula_arr[1])
            result = int(formula_arr[0]) + val

        elif formula_arr[1].isdigit():
            # get row and col from formula_arr[0]
            val = get_value_helper(formula_arr[0])
            result = int(formula_arr[1]) + val
        else:
            val1 = get_value_helper(formula_arr[0])
            val2 = get_value_helper(formula_arr[1])

            result = val1 + val2

        return result

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)