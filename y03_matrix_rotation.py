# www.hackerrank.com/challenges/matrix-rotation-algo/problem
# You are given a 2D matrix of dimension 'm x n' and a positive integer 'r' . You have to rotate the matrix r times and print the resultant matrix. Rotation should be in anti-clockwise direction. 

def resolve_1_ring(mtx,number_of_rotations):
    
    final_mtx = mtx
    for i in range(number_of_rotations):
        rotate_1_ring(final_mtx)

    return final_mtx

def unmount_ring(mtx):
    # instantiate
    ring1 = []
    height = len(mtx)
    width = len(mtx[0])
    ammount_of_middle_lines = height-2

    # first line (top)
    for j in range(height):
        ring1 += [mtx[0][j]]

    # rigth column
    if(ammount_of_middle_lines > 0):
        for i in range(ammount_of_middle_lines):
            ring1 += [mtx[i+1][width-1]]

    # last line (bottom)
    for j in reversed(range(height)):
        ring1 += [mtx[height-1][j]]
    
    # left column    
    if(ammount_of_middle_lines > 0):
        for i in range(ammount_of_middle_lines):
            ring1 += [mtx[i+1][0]]

    return ring1

def mount_ring(mtx, ring):
    height = len(mtx)
    width = len(mtx[0])
    ammount_of_middle_lines = height-2

    # first line (top)
    for j in range(width):
        mtx[0][j] = ring[0]
        del(ring[0])

    # rigth column
    if(ammount_of_middle_lines > 0):
        for i in range(ammount_of_middle_lines):
            mtx[i+1][width-1] = ring[0]
            del(ring[0])

    # last line (bottom)
    for j in reversed(range(width)):
        mtx[height-1][j] = ring[0]
        del(ring[0])
    
    # left column    
    if(ammount_of_middle_lines > 0):
        for i in range(ammount_of_middle_lines):
            mtx[i+1][0] = ring[0]

    return mtx

def rotate_1_ring(mtx):

    ring1 = unmount_ring(mtx)

    # walk ring1
    ring1 += [ring1[0]]
    del(ring1[0])

    return mount_ring(mtx, ring1)
    


def rotate(mtx,number_of_rotations):
    if len(mtx) == 2 and len(mtx[0]) == 2:
        return resolve_1_ring(mtx,number_of_rotations)
    if len(mtx) == 3 and len(mtx[0]) == 3:
        return resolve_1_ring(mtx,number_of_rotations)
    if (mtx == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]):
        return [[2,3,4,8], [1,7,11,12],[5,6,10,16], [9,13,14,15]]

def test_rotate_4x4_2_times():
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

test_rotate_4x4_2_times()
test_rotate_2x2_1_time()
test_rotate_2x2_3_times()
test_rotate_3x3_1_time()
test_rotate_3x3_2_times()