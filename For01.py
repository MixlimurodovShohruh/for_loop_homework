def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    l=[]
    for z in range(n):
        l += [z]
    return l
print(main(10))