def ivert_array(A:list, N:int):
    """"обращение массива (поворот задом-наперед)
        в рамках индексов от 0 до N-1
    """
    pass

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1, 5)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 8)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
test_invert_array()