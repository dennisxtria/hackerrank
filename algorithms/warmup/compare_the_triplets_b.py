def compareTriplets(a, b):
    alice = 0
    bob = 0

    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif y > x:
            bob += 1
        else:
            pass

    return [alice, bob]
