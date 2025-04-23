from diagonal_difference import diagonalDifference

def test1():
    input_value = "3\n1 2 3\n4 5 6\n9 8 9"

    result = diagonalDifference(input_value)
    assert result == 2

def test2():
    input_value = "4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16"
    
    result = diagonalDifference(input_value)
    assert result == 0

def test3():
    input_value = "2\n1 2\n3 4"
    
    result = diagonalDifference(input_value)
    assert result == 0

def test4():
    input_value = "3\n11 2 4\n4 5 6\n10 8 -12"
    
    result = diagonalDifference(input_value)
    assert result == 15

def test5():
    input_value = "5\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25"
    
    result = diagonalDifference(input_value)
    assert result == 0

def test6():
    input_value = "3\n-1 -2 -3\n-4 -5 -6\n-9 -8 -7"
    
    result = diagonalDifference(input_value)
    assert result == 4

def test7():
    input_value = "1\n5"
    
    result = diagonalDifference(input_value)
    assert result == 0

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    print('Successfully ran all tests')