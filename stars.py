def print_star_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

if __name__ == "__main__":
    print_star_pyramid(5)
