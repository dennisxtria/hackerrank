def diagonalDifference(arr):
    left_to_right = right_to_left = 0
    for i in range(len(arr)):
        left_to_right += arr[i][i]
        right_to_left += arr[i][len(arr) - i - 1]
    return abs(left_to_right - right_to_left)
