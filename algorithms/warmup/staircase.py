def staircase(n):
    for x in range(n):
        spaces = n - x - 1
        stars = x + 1
        print(" " * spaces + "#" * stars)
