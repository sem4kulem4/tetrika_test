def task(mass: str) -> bool | int:
    mass = list(mass)
    for index, num in enumerate(mass):
        if num == '0':
            return index
    return False


array = '111111111110000000000000000'
print(task(array))
