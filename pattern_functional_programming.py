def right_triangle(n: int) -> str:
    return '\n'.join(map(lambda i: '*' * i, range(1, n + 1)))

print(right_triangle(5))
print("-----------------")


def inverted_pyramid(n: int) -> str:
    return '\n'.join(map(
        lambda i: ' ' * i + '*' * (2 * (n - i) - 1), 
        range(n)
    ))

print(inverted_pyramid(5))
print("-----------------")



def build_pyramid(n: int, current: int = 1) -> list:
    if current > n:
        return []
    
    spaces = ' ' * (n - current)
    stars = '*' * (2 * current - 1)
    row = spaces + stars
    
    return [row] + build_pyramid(n, current + 1)

def pyramid(n: int) -> str:
    return '\n'.join(build_pyramid(n))

print(pyramid(5))
print("-----------------")


def pyramid_rows(n: int) -> list:
    return list(map(lambda i: ' ' * (n - i) + '*' * (2 * i - 1), range(1, n + 1)))

def diamond(n: int) -> str:
    rows = pyramid_rows(n)
    full_diamond = rows + rows[-2::-1]
    return '\n'.join(full_diamond)

print(diamond(5))

