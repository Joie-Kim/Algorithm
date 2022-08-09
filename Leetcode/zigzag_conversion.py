# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        row_arr = [""] * numRows
        row_idx = 0
        going_down = True

        for ch in s:
            row_arr[row_idx] += ch
            if row_idx == numRows - 1:
                going_down = False
            elif row_idx == 0:
                going_down = True
            
            if going_down:
                row_idx += 1
            else:
                row_idx -= 1
        
        return "".join(row_arr)