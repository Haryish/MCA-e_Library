def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print_move(source, target)
        return

    tower_of_hanoi(n - 1, source, auxiliary, target)
    print_move(source, target)
    tower_of_hanoi(n - 1, auxiliary, target, source)


def print_move(source, target):
    global state
    state += 1
    print(f"State {state}: A({', '.join(map(str, A))}), B({', '.join(map(str, B))}), C({', '.join(map(str, C))})")
    disk = source.pop()
    target.append(disk)


if __name__ == '__main__':
    state=0
    A,B,C=[4, 3, 2, 1],[],[] # Initial Arrangement
    print(f"Initial State: A({', '.join(map(str, A))}), B({', '.join(map(str, B))}), C({', '.join(map(str, C))})")
    tower_of_hanoi(len(A), A, C, B) # Call the recursive function to solve the Tower of Hanoi
    print(f"Final state: A({', '.join(map(str, A))}), B({', '.join(map(str, B))}), C({', '.join(map(str, C))})")
    print("No. of Iterations:", state+1)

