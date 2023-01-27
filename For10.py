def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    d=[]
    for i in list1:
        d.append(i.capitalize())
    return d

print(main(['rustam', 'diyor', 'alisher', 'bektosh']))