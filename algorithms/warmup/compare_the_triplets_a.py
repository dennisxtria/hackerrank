def compareTriplets(a, b):
    alice = (
        (1 if (a[0] > b[0]) else 0)
        + (1 if (a[1] > b[1]) else 0)
        + (1 if (a[2] > b[2]) else 0)
    )
    bob = (
        (1 if (b[0] > a[0]) else 0)
        + (1 if (b[1] > a[1]) else 0)
        + (1 if (b[2] > a[2]) else 0)
    )
    result_array = [alice, bob]

    return result_array
