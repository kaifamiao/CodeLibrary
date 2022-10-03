def tower_of_hanoi(disks: int, source: str = 'S',
                    auxiliary: str = 'A', destination: str = 'D') -> any:
    """
    Prints the steps required to transfer disks from source
    rod to destination rod.
    """
    if disks == 0:
        return
    if disks == 1:
        print('{} {}'.format(source, destination))
        return
    
    tower_of_hanoi(disks - 1, source, destination, auxiliary)
    print('{} {}'.format(source, destination))
    tower_of_hanoi(disks - 1, auxiliary, source, destination)


if __name__ == '__main__':
    tower_of_hanoi(3)