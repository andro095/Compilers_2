def indx(arr: list, element) -> int:
    try:
        return arr.index(element)
    except ValueError:
        return -1
