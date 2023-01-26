def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    a=[]
    for i in range(B, A-1,-1):
        a.append(i)
    return a
    