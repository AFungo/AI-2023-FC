def is_tuple_ordered(t):
    for i in range(len(t)-2):
        if t[i] != i+1:
            return False
    if t[len(t)-1] != 0:
        return False
    return True
