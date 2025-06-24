import math

def quadratic(a, b, c):
    """Calculate the roots of a quadratic equation ax^2 + bx + c = 0."""
    ds = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + ds) / (2 * a)
    x2 = (-b - ds) / (2 * a)
    return x1, x2


def main():
    """Main function to demonstrate the quadratic function."""
    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))





if __name__ == '__main__':
    main()



