def task(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> bool | str:
    if min(x1, x2) > max(x3, x4):
        return False
    if max(x1, x2) < min(x3, x4):
        return False
    if max(y1, y2) < min(y3, y4):
        return False
    if min(y1, y2) > max(y3, y4):
        return False
    return True


if __name__ == "__main__":
    print(task(0, 0, 1, 1, 2, 2, 3, 3))
