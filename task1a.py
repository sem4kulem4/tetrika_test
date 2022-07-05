def task(mass: str) -> bool or int:
    mass = list(mass)
    for index, num in enumerate(mass):
        if num == '0':
            return index
    return False


if __name__ == "__main__":
    array = '111111111110000000000000000'
    print(task(array))
