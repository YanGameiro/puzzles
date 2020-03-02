# www.hackerrank.com/challenges/matrix-rotation-algo/problem
# You are given a 2D matrix of dimension 'm x n' and a positive integer 'r' . You have to rotate the matrix r times and print the resultant matrix. Rotation should be in anti-clockwise direction. 

import math

def resolve_1_ring(mtx,number_of_rotations, wanted_ring):
    
    final_mtx = mtx
    for i in range(number_of_rotations):
        rotate_1_ring(final_mtx, wanted_ring)

    return final_mtx

def unmount_ring(mtx,wanted_ring):
    ring1 = []
    height = len(mtx)
    width = len(mtx[0])
    ammount_of_middle_columns = width-2 - (wanted_ring * 2)
    ammount_of_middle_lines = height-2 - (wanted_ring * 2)

    # first line (top)
    for j in range(ammount_of_middle_columns + 2):
        ring1 += [mtx[wanted_ring][j + wanted_ring]]

    # rigth column
    if ammount_of_middle_lines > 0:
        for i in range(ammount_of_middle_lines):
            ring1 += [mtx[i+wanted_ring+1][width -1 -wanted_ring]]

    # last line (bottom)
    for j in reversed(range(ammount_of_middle_columns + 2)):
        ring1 += [mtx[height - wanted_ring -1][j + wanted_ring]]

    # left column    
    if ammount_of_middle_lines > 0:
        for i in reversed(range(ammount_of_middle_lines)):
            ring1 += [mtx[i+1+ wanted_ring][wanted_ring]]
    return ring1

def mount_ring(mtx, ring, wanted_ring):
    height = len(mtx)
    width = len(mtx[0])
    ammount_of_middle_columns = width-2 - (wanted_ring * 2)
    ammount_of_middle_lines = height-2 - (wanted_ring * 2)

    # first line (top)
    for j in range(ammount_of_middle_columns + 2):
        mtx[wanted_ring][j + wanted_ring] = ring[0]
        del(ring[0])

    # rigth column
    if ammount_of_middle_lines > 0:
        for i in range(ammount_of_middle_lines):
            mtx[i+wanted_ring+1][width -1 -wanted_ring] = ring[0]
            del(ring[0])

    # last line (bottom)
    for j in reversed(range(ammount_of_middle_columns + 2)):
        mtx[height - wanted_ring -1][j + wanted_ring] = ring[0]
        del(ring[0])
    
    # left column    
    if ammount_of_middle_lines > 0:
        for i in reversed(range(ammount_of_middle_lines)):
            mtx[i+1+ wanted_ring][wanted_ring] = ring[0]
            del(ring[0])


    return mtx

def rotate_1_ring(mtx, wanted_ring):

    ring1 = unmount_ring(mtx, wanted_ring)

    # walk ring1
    ring1 += [ring1[0]]
    del(ring1[0])

    return mount_ring(mtx, ring1, wanted_ring)
    


def rotate(mtx,number_of_rotations):
    if not isinstance(mtx[0], list):
        return mtx
    smallest_measure = len(mtx) if len(mtx[0]) > len(mtx) else len(mtx[0])
    ammount_of_rings = math.floor(smallest_measure/2)
    for wanted_ring in range(ammount_of_rings):
        resolve_1_ring(mtx, number_of_rotations, wanted_ring)
    
    return mtx

def test_rotate_4x4_1_time():
    mtx = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    number_of_rotations = 1
    expected = [[2,3,4,8], [1,7,11,12],[5,6,10,16], [9,13,14,15]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected

def test_rotate_2x2_1_time():
    mtx = [[7,4],[300,5]]
    number_of_rotations = 1
    expected = [[4,5],[7,300]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected

def test_rotate_2x2_3_times():
    mtx = [[7,4],[300,5]]
    number_of_rotations = 3
    expected = [[300,7],[5,4]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected

def test_rotate_3x3_1_time():
    mtx = [[7,2,8],[4,5,1],[9,6,3]]
    number_of_rotations = 1
    expected = [[2,8,1],[7,5,3],[4,9,6]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected

def test_rotate_3x3_2_times():
    mtx = [[7,2,8],[4,5,1],[9,6,3]]
    number_of_rotations = 2
    expected = [[8,1,3],[2,5,6],[7,4,9]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected


def test_rotate_3x4_1_time():
    mtx = [[10,11,12,13],[21,22,23,24],[31,32,33,34]]
    number_of_rotations = 1
    expected = [[11,12,13,24],[10,22,23,34],[21,31,32,33]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected


def test_rotate_4x2_2_times():
    mtx = [[10,11],[21,22],[31,32],[41,42]]
    number_of_rotations = 2
    expected = [[22,32],[11,42],[10,41],[21,31]]
    result = rotate(mtx,number_of_rotations)
    assert result == expected


def test_rotate_1x1_1_time1():
    mtx = [10]
    number_of_rotations = 1
    expected = [10]
    result = rotate(mtx,number_of_rotations)
    assert result == expected

test_rotate_4x4_1_time()
test_rotate_2x2_1_time()
test_rotate_2x2_3_times()
test_rotate_3x3_1_time()
test_rotate_3x3_2_times()
test_rotate_3x4_1_time()
test_rotate_4x2_2_times()
test_rotate_1x1_1_time1()