""""
    plan:
        1. split the lines
        2. convert line 1 to int (square_size)
        3. check if no of lines - 1 is equal to value in line1
        4. create the right diagonal sum and left diagonal sum variable
        5. remove line 1 from newlines list
        6. iterate through the line enumeration
            - split by whitespace
            - check if length == line 1 value
            - add rows[row_index] to left to right sum
            - add rows[square_size-row_index-1] to right to left
        5. substract the total sums and return the result.
"""

def diagonalDifference(arg: str)->int:
    try:
        lines = arg.split('\n')
        lines_length = len(lines)
        
        if lines_length<1:
            raise ValueError("Input cannot have lines less than 2")
        
        square_size = int(lines[0].strip())

        if lines_length - 1 != square_size:
            raise Exception('Input error, no of lines does not match square value.')
        
        left_to_right_sum = 0
        right_to_left_sum = 0

        for i,val in enumerate(lines[1:]):
            row_vals = val.split(' ')
            if len(row_vals) < square_size:
                raise ValueError(f'Line {i+1} of input has missing value.')

            left_to_right_sum += int(row_vals[i])
            right_to_left_sum += int(row_vals[square_size - i - 1])

        difference = left_to_right_sum - right_to_left_sum
        return abs(difference)
    except Exception as raised_exception:
        return str(raised_exception)